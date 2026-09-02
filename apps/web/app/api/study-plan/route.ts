import { NextResponse } from "next/server";
import { toStudyPlan } from "@/lib/api";
import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET() {
  const response = await authenticatedApiFetch(
    "/api/v1/courses/rag-intensive/study-plan?horizon_days=4&daily_minutes=120",
  );
  if (!response.ok) {
    return NextResponse.json(
      { error: "Không thể tải lộ trình học." },
      { status: response.status },
    );
  }
  return NextResponse.json(toStudyPlan(await response.json()));
}
