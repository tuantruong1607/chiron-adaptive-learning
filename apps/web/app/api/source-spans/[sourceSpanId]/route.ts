import { NextResponse } from "next/server";

import { toSourceLocator } from "@/lib/api";
import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ sourceSpanId: string }> },
) {
  const { sourceSpanId } = await params;
  const response = await authenticatedApiFetch(
    `/api/v1/courses/rag-intensive/knowledge-map/sources/${encodeURIComponent(sourceSpanId)}`,
  );
  if (!response.ok) {
    return NextResponse.json(
      {
        error:
          response.status === 404
            ? "Không tìm thấy nguồn trong graph hiện tại."
            : "Không thể tải source locator.",
      },
      { status: response.status },
    );
  }
  return NextResponse.json(toSourceLocator(await response.json()));
}
