"use client";

import type { SourceLocator as SourceLocatorData } from "@chiron/domain";
import Link from "next/link";
import React, { useEffect, useState } from "react";

export function SourceLocator({ sourceSpanId }: { sourceSpanId: string }) {
  const [citation, setCitation] = useState<SourceLocatorData | null>(null);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    const controller = new AbortController();
    setCitation(null);
    setError(null);
    fetch(`/api/source-spans/${encodeURIComponent(sourceSpanId)}`, {
      cache: "no-store",
      signal: controller.signal,
    })
      .then(async (response) => {
        if (!response.ok) {
          const payload = (await response.json().catch(() => null)) as {
            error?: string;
          } | null;
          throw new Error(payload?.error ?? "Không thể tải source locator.");
        }
        return (await response.json()) as SourceLocatorData;
      })
      .then(setCitation)
      .catch((reason: Error) => {
        if (reason.name !== "AbortError") setError(reason.message);
      });
    return () => controller.abort();
  }, [sourceSpanId]);

  if (error)
    return (
      <div className="glass-surface source-state" role="alert">
        {error}
      </div>
    );
  if (!citation)
    return (
      <div className="glass-surface source-state">Đang tải source locator…</div>
    );
  return (
    <article className="glass-surface source-card">
      <p className="eyebrow">Source span</p>
      <h2>{citation.title}</h2>
      <span className="concept-status">{citation.locator}</span>
      <dl className="source-details">
        <div>
          <dt>Loại nguồn</dt>
          <dd>{citation.sourceType}</dd>
        </div>
        {citation.page !== null && (
          <div>
            <dt>Trang</dt>
            <dd>{citation.page}</dd>
          </div>
        )}
        {citation.sectionTitle && (
          <div>
            <dt>Mục</dt>
            <dd>{citation.sectionTitle}</dd>
          </div>
        )}
        {citation.sourceFile && (
          <div>
            <dt>Tệp nguồn</dt>
            <dd>{citation.sourceFile}</dd>
          </div>
        )}
        {citation.heading && (
          <div>
            <dt>Tiêu đề mục</dt>
            <dd>{citation.heading}</dd>
          </div>
        )}
        {citation.sectionId && (
          <div>
            <dt>Section ID</dt>
            <dd>{citation.sectionId}</dd>
          </div>
        )}
        {citation.order !== null && (
          <div>
            <dt>Thứ tự mục</dt>
            <dd>{citation.order}</dd>
          </div>
        )}
        {citation.extractionMethod && (
          <div>
            <dt>Trích xuất</dt>
            <dd>{citation.extractionMethod}</dd>
          </div>
        )}
      </dl>
      <p>{citation.excerpt}</p>
      <code>{citation.sourceSpanId}</code>
      <Link className="text-link" href="/map">
        Quay lại bản đồ kiến thức
      </Link>
    </article>
  );
}
