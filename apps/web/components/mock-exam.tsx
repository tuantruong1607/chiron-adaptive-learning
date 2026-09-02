"use client";

import {
  ArrowLeft,
  ArrowRight,
  BookmarkSimple,
  Check,
  CheckCircle,
  Clock,
  Exam,
  Eye,
  FileText,
  FloppyDisk,
  Sparkle,
  Target,
  Warning,
  WarningCircle,
  XCircle,
} from "@phosphor-icons/react";
import React, { useEffect, useMemo, useState } from "react";

type ObjectiveQuestion = {
  id: string;
  number: number;
  kind: "objective";
  title: string;
  topic: string;
  difficulty: string;
  prompt: string;
  options: Array<{ id: string; text: string }>;
};

type ConstructedQuestion = {
  id: string;
  number: number;
  kind: "constructed";
  title: string;
  topic: string;
  difficulty: string;
  prompt: string;
  rubric: string;
};

type Question = ObjectiveQuestion | ConstructedQuestion;
type Answer = { optionId?: string; text?: string; flagged?: boolean };

type ExamPayload = {
  form_id: string;
  title: string;
  duration_minutes: number;
  questions: Question[];
};

type ObjectiveReview = {
  question_id: string;
  selected_option_id?: string;
  correct_option_id?: string;
  explanation: string;
};

type ConstructedReview = {
  question_id: string;
  score: number;
  max_score: number;
  normalized_score: number;
  feedback: string;
  confidence: number;
  provider: string;
};

type ExamResult = {
  form_id: string;
  score: number;
  total?: number;
  objective_score: number;
  objective_total?: number;
  constructed_score: number;
  constructed_total?: number;
  grading_mode: "llm" | "hybrid" | "deterministic";
  providers: string[];
  objective_reviews: ObjectiveReview[];
  constructed_reviews: ConstructedReview[];
};

const forms = ["de-01", "de-02", "de-03", "de-04"];

export function MockExam() {
  const [exam, setExam] = useState<ExamPayload | null>(null);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, Answer>>({});
  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<ExamResult | null>(null);
  const [startedAt, setStartedAt] = useState<number | null>(null);
  const [now, setNow] = useState(Date.now());
  const [draftForms, setDraftForms] = useState<Set<string>>(new Set());
  const [activeTab, setActiveTab] = useState<"overview" | "objective" | "constructed">("overview");
  const [filterTopic, setFilterTopic] = useState<string>("all");
  const [showConfirmSubmit, setShowConfirmSubmit] = useState(false);

  useEffect(() => {
    setDraftForms(
      new Set(
        forms.filter((formId) =>
          localStorage.getItem(`chiron-mock-exam-${formId}`),
        ),
      ),
    );
  }, []);

  useEffect(() => {
    if (!startedAt || result) return;
    const timer = window.setInterval(() => setNow(Date.now()), 10_000);
    return () => window.clearInterval(timer);
  }, [result, startedAt]);

  useEffect(() => {
    if (!exam) return;
    localStorage.setItem(
      `chiron-mock-exam-${exam.form_id}`,
      JSON.stringify({ answers, index, startedAt }),
    );
  }, [answers, exam, index, startedAt]);

  const answeredCount = useMemo(() => {
    return Object.values(answers).filter(
      (answer) => answer.optionId || (answer.text?.trim().length ?? 0) >= 2,
    ).length;
  }, [answers]);

  const flaggedCount = useMemo(() => {
    return Object.values(answers).filter((answer) => answer.flagged).length;
  }, [answers]);

  const remainingMinutes = useMemo(() => {
    if (!startedAt) return 120;
    const elapsedMinutes = Math.floor((now - startedAt) / 60_000);
    return Math.max(0, 120 - elapsedMinutes);
  }, [now, startedAt]);

  const topicsList = useMemo(() => {
    if (!exam) return [];
    const set = new Set(exam.questions.map((q) => q.topic));
    return ["all", ...Array.from(set)];
  }, [exam]);

  async function startExam(formId: string) {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`/api/mock-exams/${formId}`, {
        cache: "no-store",
      });
      if (!response.ok) throw new Error("Exam unavailable");
      const payload: ExamPayload = await response.json();
      const saved = localStorage.getItem(`chiron-mock-exam-${formId}`);
      if (saved) {
        try {
          const draft = JSON.parse(saved);
          setAnswers(draft.answers ?? {});
          setIndex(Math.min(draft.index ?? 0, (payload.questions?.length ?? 100) - 1));
          setStartedAt(draft.startedAt ?? Date.now());
        } catch {
          localStorage.removeItem(`chiron-mock-exam-${formId}`);
          setStartedAt(Date.now());
        }
      } else {
        setAnswers({});
        setIndex(0);
        setStartedAt(Date.now());
      }
      setNow(Date.now());
      setExam(payload);
    } catch {
      setError("Không thể tải đề thi. Vui lòng thử lại.");
    } finally {
      setLoading(false);
    }
  }

  async function submitExam() {
    if (!exam) return;
    setSubmitting(true);
    setError(null);
    setShowConfirmSubmit(false);
    try {
      const response = await fetch(`/api/mock-exams/${exam.form_id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          answers: exam.questions.map((question) => ({
            question_id: question.id,
            option_id: answers[question.id]?.optionId,
            text: answers[question.id]?.text,
          })),
        }),
      });
      if (!response.ok) throw new Error("Grading failed");
      const res: ExamResult = await response.json();
      setResult(res);
      localStorage.removeItem(`chiron-mock-exam-${exam.form_id}`);
    } catch {
      setError("Chưa thể chấm bài thi lúc này. Bản nháp bài làm vẫn được lưu trữ an toàn trên máy của bạn.");
    } finally {
      setSubmitting(false);
    }
  }

  const toggleFlag = (questionId: string) => {
    setAnswers((prev) => ({
      ...prev,
      [questionId]: {
        ...prev[questionId],
        flagged: !prev[questionId]?.flagged,
      },
    }));
  };

  // 1. Catalog screen
  if (!exam) {
    return (
      <section className="exam-catalog" aria-labelledby="exam-catalog-title">
        <div className="exam-catalog-intro">
          <span className="badge badge-accent">Khảo sát & Chuẩn hóa Năng lực</span>
          <h2 id="exam-catalog-title">Ngân hàng 4 Đề Thi Thử Chuẩn Hóa · 100 Câu</h2>
          <p>
            Cấu trúc chuẩn theo blueprint: 90 câu trắc nghiệm kịch bản & phân tích (chấm điểm tức thì) 
            và 10 câu tự luận chuyên sâu (chấm tự động theo rubric đa tiêu chí qua LLM-as-Judge).
          </p>
        </div>
        <div className="exam-form-grid">
          {forms.map((formId, formIndex) => (
            <article key={formId} className="exam-card">
              <div className="exam-card-header">
                <div className="exam-icon-wrapper">
                  <Exam size={28} weight="duotone" />
                </div>
                <span className="exam-form-code">Mã đề {String(formIndex + 1).padStart(2, "0")}</span>
              </div>
              <h3>Đề Thi Thử Toàn Diện {String(formIndex + 1).padStart(2, "0")}</h3>
              <ul className="exam-specs-list">
                <li>⏱ Thời gian: 120 phút</li>
                <li>📝 90 câu trắc nghiệm + 10 câu tự luận</li>
                <li>⚡ Chấm điểm & nhận xét tức thì khi nộp bài</li>
              </ul>
              <button
                type="button"
                className="button button-primary"
                disabled={loading}
                onClick={() => startExam(formId)}
              >
                {draftForms.has(formId) ? "Tiếp tục làm bài dở" : "Bắt đầu làm bài"}
                <ArrowRight size={18} weight="bold" />
              </button>
            </article>
          ))}
        </div>
        {error && (
          <p className="form-error" role="alert">
            <WarningCircle size={20} /> {error}
          </p>
        )}
      </section>
    );
  }

  // 2. Result screen (Instant feedback)
  if (result) {
    const objectiveQuestions = exam.questions.filter((q) => q.kind === "objective");
    const constructedQuestions = exam.questions.filter((q) => q.kind === "constructed");
    const wrongMap = new Map(result.objective_reviews.map((r) => [r.question_id, r]));

    return (
      <section className="mock-result-container">
        <header className="mock-result-hero">
          <div className="mock-result-hero-content">
            <span className="badge badge-accent">Kết quả Đề thi {exam.title}</span>
            <div className="score-hero-display">
              <span className="score-number">{result.score.toFixed(1)}</span>
              <span className="score-scale">/ 100</span>
            </div>
            <div className="score-badge-pill">
              {result.score >= 80 ? (
                <span className="pill-success">🎉 Xuất sắc — Đạt chuẩn Production</span>
              ) : result.score >= 65 ? (
                <span className="pill-warning">⚡ Khá — Cần rà soát một số topic</span>
              ) : (
                <span className="pill-danger">🎯 Cần củng cố kiến thức trọng tâm</span>
              )}
            </div>
          </div>

          <div className="mock-result-metrics-grid">
            <div className="metric-box">
              <span className="metric-box-label">Trắc nghiệm</span>
              <strong className="metric-box-value">
                {result.objective_score} / {result.objective_total ?? objectiveQuestions.length}
              </strong>
              <span className="metric-box-sub">
                Đúng {result.objective_score}/{objectiveQuestions.length} câu
              </span>
            </div>

            <div className="metric-box">
              <span className="metric-box-label">Tự luận (LLM Judge)</span>
              <strong className="metric-box-value">
                {result.constructed_score.toFixed(1)} / {result.constructed_total ?? constructedQuestions.length}
              </strong>
              <span className="metric-box-sub">10 câu theo Rubric đa tiêu chí</span>
            </div>

            <div className="metric-box">
              <span className="metric-box-label">Cơ chế chấm</span>
              <strong className="metric-box-value highlight-text">
                {result.grading_mode === "llm" ? "⚡ LLM-as-Judge" : "⚙️ Rubric Deterministic"}
              </strong>
              <span className="metric-box-sub">Phản hồi tự động tức thì</span>
            </div>
          </div>
        </header>

        {/* Tab Navigation */}
        <nav className="result-tab-nav" aria-label="Phân tích kết quả">
          <button
            type="button"
            className={`tab-btn ${activeTab === "overview" ? "active" : ""}`}
            onClick={() => setActiveTab("overview")}
          >
            <Target size={18} /> Tổng quan & Đề xuất
          </button>
          <button
            type="button"
            className={`tab-btn ${activeTab === "objective" ? "active" : ""}`}
            onClick={() => setActiveTab("objective")}
          >
            <CheckCircle size={18} /> Chi tiết Trắc nghiệm ({objectiveQuestions.length})
          </button>
          <button
            type="button"
            className={`tab-btn ${activeTab === "constructed" ? "active" : ""}`}
            onClick={() => setActiveTab("constructed")}
          >
            <FileText size={18} /> Chi tiết Tự luận ({constructedQuestions.length})
          </button>
        </nav>

        {/* Tab 1: Overview */}
        {activeTab === "overview" && (
          <div className="result-tab-content">
            <div className="result-overview-card">
              <h3>🎯 Đánh giá tổng quan & Kế hoạch ôn tập tiếp theo</h3>
              <p>
                Bạn đã hoàn thành bài thi 100 câu. Kết quả trắc nghiệm và đánh giá tự luận đã được phân tích.
                Hãy chú ý các câu trả lời sai và nhận xét của LLM Judge để củng cố các lỗ hổng kiến thức trước khi bước vào kỳ thi thực tế.
              </p>
              <div className="next-steps-banner">
                <Sparkle size={24} weight="duotone" className="sparkle-icon" />
                <div>
                  <strong>Khuyến nghị từ Chiron AI:</strong>
                  <p>
                    Truy cập <strong>Knowledge Map</strong> để xem trực quan các concept cần nâng cao điểm mastery 
                    và tra cứu lại nguồn trích dẫn gốc (source locators) từ giáo trình.
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Tab 2: Objective Questions Review */}
        {activeTab === "objective" && (
          <div className="result-tab-content">
            <div className="review-list">
              {objectiveQuestions.map((q, idx) => {
                const userAns = answers[q.id]?.optionId;
                const wrongInfo = wrongMap.get(q.id);
                const isCorrect = !wrongInfo;

                return (
                  <article
                    key={q.id}
                    className={`review-item-card ${isCorrect ? "review-correct" : "review-incorrect"}`}
                  >
                    <header className="review-item-header">
                      <div className="review-title-group">
                        <span className="question-num-pill">Câu {idx + 1}</span>
                        <span className="topic-pill">{q.topic}</span>
                      </div>
                      <div className="status-pill">
                        {isCorrect ? (
                          <span className="badge badge-success">
                            <Check size={14} weight="bold" /> Đúng (+1.0đ)
                          </span>
                        ) : (
                          <span className="badge badge-error">
                            <XCircle size={14} weight="bold" /> Sai (0đ)
                          </span>
                        )}
                      </div>
                    </header>

                    <div className="review-prompt">{q.prompt}</div>

                    <div className="review-options">
                      {q.options.map((opt) => {
                        const isUserSelected = userAns === opt.id;
                        const isTheCorrectOpt = wrongInfo ? wrongInfo.correct_option_id === opt.id : isUserSelected;

                        return (
                          <div
                            key={opt.id}
                            className={`review-option-row ${
                              isTheCorrectOpt ? "opt-correct" : isUserSelected ? "opt-wrong" : ""
                            }`}
                          >
                            <span className="opt-key">{opt.id.toUpperCase()}</span>
                            <span className="opt-text">{opt.text}</span>
                            {isTheCorrectOpt && <span className="opt-badge">Đáp án đúng</span>}
                            {isUserSelected && !isTheCorrectOpt && (
                              <span className="opt-badge opt-badge-wrong">Bạn đã chọn</span>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {wrongInfo && wrongInfo.explanation && (
                      <div className="review-explanation">
                        <strong>💡 Giải thích chi tiết:</strong>
                        <p>{wrongInfo.explanation}</p>
                      </div>
                    )}
                  </article>
                );
              })}
            </div>
          </div>
        )}

        {/* Tab 3: Constructed Questions Review (LLM as Judge) */}
        {activeTab === "constructed" && (
          <div className="result-tab-content">
            <div className="constructed-review-list">
              {result.constructed_reviews.map((rev, revIdx) => {
                const questionObj = constructedQuestions.find((q) => q.id === rev.question_id);
                const userAnswerText = answers[rev.question_id]?.text ?? "";

                return (
                  <article key={rev.question_id} className="constructed-review-card">
                    <header className="constructed-card-header">
                      <div>
                        <span className="question-num-pill">Câu Tự luận {revIdx + 1}</span>
                        <span className="topic-pill">{questionObj?.topic ?? "Kiến trúc & Thiết kế"}</span>
                      </div>
                      <div className="score-tag">
                        <strong>
                          Điểm quy đổi: {rev.normalized_score.toFixed(2)} / 1.00 đ
                        </strong>
                        <span className="raw-score">
                          (Thang rubric: {rev.score}/{rev.max_score})
                        </span>
                      </div>
                    </header>

                    <div className="constructed-prompt">{questionObj?.prompt}</div>

                    <div className="user-submission-box">
                      <span className="box-label">Bài làm của bạn:</span>
                      <p className="submission-text">
                        {userAnswerText.trim() ? userAnswerText : <em>(Chưa nhập câu trả lời)</em>}
                      </p>
                    </div>

                    <div className="ai-feedback-box">
                      <div className="ai-feedback-header">
                        <Sparkle size={18} weight="duotone" />
                        <span>Đánh giá từ AI Judge ({rev.provider}):</span>
                      </div>
                      <p className="feedback-content">{rev.feedback}</p>
                    </div>

                    {questionObj?.rubric && (
                      <details className="rubric-details">
                        <summary>Xem tiêu chí chấm (Rubric chuẩn)</summary>
                        <p>{questionObj.rubric}</p>
                      </details>
                    )}
                  </article>
                );
              })}
            </div>
          </div>
        )}

        {/* Actions footer */}
        <div className="exam-actions result-actions">
          <button
            className="button button-secondary"
            type="button"
            onClick={() => {
              setExam(null);
              setResult(null);
            }}
          >
            ← Quay lại danh mục đề thi
          </button>
          <a className="button button-primary" href="/map">
            Mở Knowledge Map ôn luyện <ArrowRight size={18} weight="bold" />
          </a>
        </div>
      </section>
    );
  }

  // 3. Active Exam workspace
  const question = exam.questions[index];
  const isObjective = question.kind === "objective";
  const currentAnswer = answers[question.id] || {};
  const isFlagged = Boolean(currentAnswer.flagged);

  return (
    <section className="mock-exam-shell" aria-labelledby="active-exam-title">
      <header className="mock-exam-status">
        <div className="exam-status-left">
          <span className="exam-badge-chip">{exam.title}</span>
          <h2 id="active-exam-title" className="current-q-title">
            Câu {index + 1} <small>/ {exam.questions.length}</small>
          </h2>
        </div>

        <div className="exam-status-center">
          <div className={`timer-box ${remainingMinutes < 15 ? "timer-critical" : ""}`}>
            <Clock size={20} weight="duotone" />
            <span>Còn {remainingMinutes} phút</span>
          </div>
        </div>

        <div className="exam-status-right">
          <div className="progress-stat">
            <FloppyDisk size={18} />
            <span>Đã làm: {answeredCount}/{exam.questions.length}</span>
          </div>
          <button
            type="button"
            className="button button-primary button-sm"
            onClick={() => setShowConfirmSubmit(true)}
          >
            Nộp bài
          </button>
        </div>
      </header>

      <div className="mock-exam-layout">
        {/* Sidebar Question Palette */}
        <aside className="question-palette-panel" aria-label="Bảng câu hỏi 1-100">
          <div className="palette-header">
            <h3>Bảng câu hỏi ({answeredCount}/100)</h3>
            {flaggedCount > 0 && (
              <span className="flag-count-pill">
                <BookmarkSimple size={14} weight="fill" /> {flaggedCount} đã đánh dấu
              </span>
            )}
          </div>

          <div className="palette-filter">
            <select
              value={filterTopic}
              onChange={(e) => setFilterTopic(e.target.value)}
              aria-label="Lọc câu hỏi theo chủ đề"
            >
              <option value="all">Tất cả chủ đề</option>
              {topicsList
                .filter((t) => t !== "all")
                .map((topic) => (
                  <option key={topic} value={topic}>
                    {topic}
                  </option>
                ))}
            </select>
          </div>

          <div className="question-grid">
            {exam.questions.map((item, itemIndex) => {
              if (filterTopic !== "all" && item.topic !== filterTopic) return null;

              const ans = answers[item.id];
              const isAnswered = Boolean(ans?.optionId || (ans?.text?.trim().length ?? 0) >= 2);
              const flagged = Boolean(ans?.flagged);
              const isCurrent = itemIndex === index;

              return (
                <button
                  type="button"
                  key={item.id}
                  className={`palette-btn ${isCurrent ? "current" : ""} ${isAnswered ? "answered" : ""} ${flagged ? "flagged" : ""}`}
                  onClick={() => setIndex(itemIndex)}
                  aria-label={`Đi tới câu ${itemIndex + 1}`}
                  aria-current={isCurrent ? "step" : undefined}
                >
                  <span className="btn-number">{itemIndex + 1}</span>
                  {flagged && <span className="flag-dot" />}
                  {isAnswered && !flagged && <Check size={10} weight="bold" className="answered-icon" />}
                </button>
              );
            })}
          </div>

          <div className="palette-legend">
            <span className="legend-item"><span className="legend-box answered" /> Đã làm</span>
            <span className="legend-item"><span className="legend-box current" /> Đang xem</span>
            <span className="legend-item"><span className="legend-box flagged" /> Đánh dấu</span>
          </div>
        </aside>

        {/* Main Question Workspace */}
        <main className="mock-question-panel">
          <div className="mock-question-header">
            <div className="meta-left">
              <span className="badge badge-type">
                {isObjective ? "Trắc nghiệm · 1.0 điểm" : "Tự luận chuyên sâu · 1.0 điểm quy đổi"}
              </span>
              <span className="badge badge-topic">{question.topic}</span>
              <span className="badge badge-diff">{question.difficulty}</span>
            </div>

            <button
              type="button"
              className={`flag-toggle-btn ${isFlagged ? "active" : ""}`}
              onClick={() => toggleFlag(question.id)}
            >
              <BookmarkSimple size={18} weight={isFlagged ? "fill" : "regular"} />
              {isFlagged ? "Bỏ đánh dấu" : "Đánh dấu xem lại"}
            </button>
          </div>

          <div className="prompt-container">
            <div className="prompt-text">{question.prompt}</div>
          </div>

          {isObjective ? (
            <div className="answer-options-group" role="radiogroup" aria-label="Các lựa chọn đáp án">
              {(question as ObjectiveQuestion).options.map((option) => {
                const isSelected = currentAnswer.optionId === option.id;

                return (
                  <button
                    type="button"
                    role="radio"
                    aria-checked={isSelected}
                    key={option.id}
                    className={`option-choice-card ${isSelected ? "selected" : ""}`}
                    onClick={() =>
                      setAnswers((current) => ({
                        ...current,
                        [question.id]: { ...current[question.id], optionId: option.id },
                      }))
                    }
                  >
                    <div className="option-indicator">
                      <span>{option.id.toUpperCase()}</span>
                    </div>
                    <div className="option-text-body">{option.text}</div>
                  </button>
                );
              })}
            </div>
          ) : (
            <div className="constructed-editor-container">
              <label htmlFor={`answer-${question.id}`} className="editor-label">
                Trình bày câu trả lời của bạn:
              </label>
              <textarea
                id={`answer-${question.id}`}
                rows={9}
                value={currentAnswer.text ?? ""}
                onChange={(event) =>
                  setAnswers((current) => ({
                    ...current,
                    [question.id]: { ...current[question.id], text: event.target.value },
                  }))
                }
                placeholder="Trình bày giải pháp thiết kế, trade-offs, các cơ chế kiểm soát rủi ro và cách thức kiểm chứng..."
                className="constructed-textarea"
              />
              <div className="editor-footer">
                <span className="word-counter">
                  {(currentAnswer.text?.trim().split(/\s+/).filter(Boolean).length ?? 0)} từ
                </span>
                <details className="rubric-preview">
                  <summary>
                    <Eye size={16} /> Xem tiêu chí chấm điểm (Rubric)
                  </summary>
                  <p>{(question as ConstructedQuestion).rubric}</p>
                </details>
              </div>
            </div>
          )}

          {/* Question navigation footer */}
          <footer className="mock-question-footer">
            <button
              className="button button-secondary"
              type="button"
              disabled={index === 0}
              onClick={() => setIndex((value) => value - 1)}
            >
              <ArrowLeft size={18} /> Câu trước
            </button>

            <div className="footer-actions-right">
              {index < exam.questions.length - 1 ? (
                <button
                  className="button button-primary"
                  type="button"
                  onClick={() => setIndex((value) => value + 1)}
                >
                  Câu tiếp theo <ArrowRight size={18} />
                </button>
              ) : (
                <button
                  className="button button-primary submit-highlight-btn"
                  type="button"
                  disabled={submitting}
                  onClick={() => setShowConfirmSubmit(true)}
                >
                  {submitting ? "Đang chấm bài..." : `Nộp bài thi (${answeredCount}/100)`}
                </button>
              )}
            </div>
          </footer>

          {error && (
            <p className="form-error" role="alert">
              <WarningCircle size={18} /> {error}
            </p>
          )}
        </main>
      </div>

      {/* Confirmation Modal */}
      {showConfirmSubmit && (
        <div className="modal-backdrop" role="dialog" aria-modal="true">
          <div className="confirm-modal-box">
            <div className="modal-icon">
              <Warning size={32} weight="duotone" />
            </div>
            <h3>Xác nhận nộp bài thi?</h3>
            <p>
              Bạn đã hoàn thành <strong>{answeredCount} / {exam.questions.length}</strong> câu hỏi.
              {answeredCount < exam.questions.length && (
                <span> Vẫn còn <strong>{exam.questions.length - answeredCount}</strong> câu chưa điền câu trả lời.</span>
              )}
            </p>
            <p className="modal-sub">
              Sau khi nộp, hệ thống sẽ chấm điểm tức thì toàn bộ bài làm và sinh nhận xét chi tiết qua LLM-as-Judge.
            </p>
            <div className="modal-actions">
              <button
                type="button"
                className="button button-secondary"
                onClick={() => setShowConfirmSubmit(false)}
              >
                Tiếp tục làm bài
              </button>
              <button
                type="button"
                className="button button-primary"
                disabled={submitting}
                onClick={submitExam}
              >
                {submitting ? "Đang chấm..." : "Xác nhận nộp ngay"}
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
