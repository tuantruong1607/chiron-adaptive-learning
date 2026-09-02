# Chiron RAGAS retrieval baseline

- Dataset: `eval\rag\golden.jsonl`
- Cases: **35**
- Collection: `chiron_chunks_v1`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **FAIL**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | 0.886 | 0.624 | 0.571 | 0.437 | 0.126 | 0.624 | 295.4 |
| graph_lite | 0.914 | 0.614 | 0.556 | 0.428 | 0.126 | 0.614 | 323.3 |

## By query class

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 1.000 | 0.933 | 0.769 | 0.635 |
| prerequisite | 10 | 0.800 | 0.400 | 0.432 | 0.285 |
| multi_hop | 10 | 0.800 | 0.383 | 0.412 | 0.292 |

### graph_lite

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 1.000 | 0.933 | 0.802 | 0.650 |
| prerequisite | 10 | 0.800 | 0.400 | 0.381 | 0.267 |
| multi_hop | 10 | 0.900 | 0.350 | 0.362 | 0.255 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `35`, expected `= 35`
- **PASS** `all_cases_human_approved` — actual `35`, expected `= 35`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `35`, expected `= 35`
- **PASS** `coverage_direct` — actual `15`, expected `= 15`
- **PASS** `coverage_prerequisite` — actual `10`, expected `= 10`
- **PASS** `coverage_multi_hop` — actual `10`, expected `= 10`
- **PASS** `graph_lite_p95_within_budget` — actual `323.3`, expected `<= 500 ms`
- **PASS** `graph_lite_direct_recall_gate` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `graph_lite_prerequisite_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
- **FAIL** `graph_lite_multi_hop_recall_gate` — actual `-0.0333`, expected `>= 0 recall delta`
