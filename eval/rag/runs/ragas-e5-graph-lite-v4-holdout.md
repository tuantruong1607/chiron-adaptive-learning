# Chiron RAGAS retrieval baseline

- Dataset: `eval\rag\golden.jsonl`
- Cases: **15**
- Collection: `chiron_chunks_v1`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **PASS**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | 0.867 | 0.600 | 0.517 | 0.434 | 0.167 | 0.600 | 377.7 |
| graph_lite | 0.867 | 0.600 | 0.551 | 0.446 | 0.167 | 0.600 | 332.0 |

## By query class

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 1.000 | 1.000 | 0.507 | 0.598 |
| prerequisite | 5 | 0.800 | 0.500 | 0.379 | 0.311 |
| multi_hop | 5 | 0.800 | 0.300 | 0.667 | 0.393 |

### graph_lite

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 1.000 | 1.000 | 0.607 | 0.633 |
| prerequisite | 5 | 0.800 | 0.500 | 0.379 | 0.311 |
| multi_hop | 5 | 0.800 | 0.300 | 0.667 | 0.393 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `15`, expected `= 15`
- **PASS** `all_cases_have_resolved_source_labels` — actual `15`, expected `= 15`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `15`, expected `= 15`
- **PASS** `coverage_direct` — actual `5`, expected `= 5`
- **PASS** `coverage_prerequisite` — actual `5`, expected `= 5`
- **PASS** `coverage_multi_hop` — actual `5`, expected `= 5`
- **PASS** `graph_lite_p95_within_budget` — actual `332.0`, expected `<= 500 ms`
- **PASS** `graph_lite_direct_recall_gate` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `graph_lite_prerequisite_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
- **PASS** `graph_lite_multi_hop_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
