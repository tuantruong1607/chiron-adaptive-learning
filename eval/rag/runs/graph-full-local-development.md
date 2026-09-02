# Chiron RAGAS retrieval baseline

- Dataset: `/workspace/eval/rag/golden-local.jsonl`
- Cases: **35**
- Collection: `chiron_chunks_v1_full`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **FAIL**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | 0.514 | 0.290 | 0.314 | 0.230 | 0.060 | 0.290 | 1284.6 |
| graph_lite | 0.486 | 0.281 | 0.324 | 0.231 | 0.057 | 0.281 | 917.8 |

## By query class

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 0.600 | 0.467 | 0.469 | 0.371 |
| prerequisite | 10 | 0.500 | 0.200 | 0.283 | 0.172 |
| multi_hop | 10 | 0.400 | 0.117 | 0.113 | 0.076 |

### graph_lite

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 0.600 | 0.467 | 0.469 | 0.371 |
| prerequisite | 10 | 0.500 | 0.200 | 0.287 | 0.173 |
| multi_hop | 10 | 0.300 | 0.083 | 0.145 | 0.079 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `35`, expected `= 35`
- **PASS** `all_cases_have_resolved_source_labels` — actual `35`, expected `= 35`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `35`, expected `= 35`
- **PASS** `coverage_direct` — actual `15`, expected `= 15`
- **PASS** `coverage_prerequisite` — actual `10`, expected `= 10`
- **PASS** `coverage_multi_hop` — actual `10`, expected `= 10`
- **FAIL** `graph_lite_p95_within_budget` — actual `917.8`, expected `<= 500 ms`
- **PASS** `graph_lite_direct_recall_gate` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `graph_lite_prerequisite_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
- **FAIL** `graph_lite_multi_hop_recall_gate` — actual `-0.0333`, expected `>= 0 recall delta`
