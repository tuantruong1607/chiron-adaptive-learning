# Chiron RAGAS retrieval baseline

- Dataset: `eval/rag/golden-local.jsonl`
- Cases: **35**
- Collection: `chiron_chunks_v1_full`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **PASS**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | 0.714 | 0.476 | 0.368 | 0.294 | 0.089 | 0.476 | 569.4 |
| graph_lite | 0.714 | 0.476 | 0.368 | 0.294 | 0.089 | 0.476 | 461.7 |

## By query class

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 0.867 | 0.800 | 0.523 | 0.455 |
| prerequisite | 10 | 0.600 | 0.250 | 0.314 | 0.209 |
| multi_hop | 10 | 0.600 | 0.217 | 0.188 | 0.138 |

### graph_lite

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 0.867 | 0.800 | 0.523 | 0.455 |
| prerequisite | 10 | 0.600 | 0.250 | 0.314 | 0.209 |
| multi_hop | 10 | 0.600 | 0.217 | 0.188 | 0.138 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `35`, expected `= 35`
- **PASS** `all_cases_have_resolved_source_labels` — actual `35`, expected `= 35`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `35`, expected `= 35`
- **PASS** `coverage_direct` — actual `15`, expected `= 15`
- **PASS** `coverage_prerequisite` — actual `10`, expected `= 10`
- **PASS** `coverage_multi_hop` — actual `10`, expected `= 10`
- **PASS** `graph_lite_p95_within_budget` — actual `461.7`, expected `<= 500 ms`
- **PASS** `graph_lite_direct_recall_gate` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `graph_lite_prerequisite_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
- **PASS** `graph_lite_multi_hop_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
