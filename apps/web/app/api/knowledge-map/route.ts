import { NextResponse } from "next/server";
import { toKnowledgeMap } from "@/lib/api";
import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET() {
  const response = await authenticatedApiFetch(
    "/api/v1/courses/rag-intensive/knowledge-map",
  );
  if (!response.ok) {
    return NextResponse.json(
      { error: "Không thể tải bản đồ kiến thức." },
      { status: response.status },
    );
  }
  return NextResponse.json(toKnowledgeMap(await response.json()));
}
