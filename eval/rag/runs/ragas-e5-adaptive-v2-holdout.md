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
| dense | 0.800 | 0.567 | 0.541 | 0.413 | 0.140 | 0.567 | 262.6 |
| bm25 | 0.800 | 0.311 | 0.458 | 0.326 | 0.120 | 0.311 | 210.5 |
| hybrid | 0.867 | 0.600 | 0.517 | 0.434 | 0.167 | 0.600 | 230.2 |
| adaptive | 0.867 | 0.600 | 0.551 | 0.446 | 0.167 | 0.600 | 251.3 |

## By query class

### dense

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 1.000 | 1.000 | 0.767 | 0.725 |
| prerequisite | 5 | 0.800 | 0.400 | 0.407 | 0.266 |
| multi_hop | 5 | 0.600 | 0.300 | 0.450 | 0.247 |

### bm25

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 1.000 | 0.400 | 0.423 | 0.394 |
| prerequisite | 5 | 0.600 | 0.300 | 0.350 | 0.257 |
| multi_hop | 5 | 0.800 | 0.233 | 0.600 | 0.326 |

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 1.000 | 1.000 | 0.507 | 0.598 |
| prerequisite | 5 | 0.800 | 0.500 | 0.379 | 0.311 |
| multi_hop | 5 | 0.800 | 0.300 | 0.667 | 0.393 |

### adaptive

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 1.000 | 1.000 | 0.607 | 0.633 |
| prerequisite | 5 | 0.800 | 0.500 | 0.379 | 0.311 |
| multi_hop | 5 | 0.800 | 0.300 | 0.667 | 0.393 |

## Largest adaptive recall regressions

| Case | Class | Hybrid recall | Adaptive recall | Delta |
| --- | --- | ---: | ---: | ---: |
| ret-045 | multi_hop | 0.500 | 0.500 | +0.000 |
| ret-047 | multi_hop | 0.000 | 0.000 | +0.000 |
| ret-016 | multi_hop | 0.000 | 0.000 | +0.000 |
| ret-020 | multi_hop | 0.333 | 0.333 | +0.000 |
| ret-043 | multi_hop | 0.667 | 0.667 | +0.000 |
| ret-027 | direct | 1.000 | 1.000 | +0.000 |
| ret-009 | prerequisite | 0.500 | 0.500 | +0.000 |
| ret-001 | direct | 1.000 | 1.000 | +0.000 |
| ret-007 | direct | 1.000 | 1.000 | +0.000 |
| ret-034 | prerequisite | 0.500 | 0.500 | +0.000 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `15`, expected `= 15`
- **PASS** `all_cases_human_approved` — actual `15`, expected `= 15`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `15`, expected `= 15`
- **PASS** `coverage_direct` — actual `5`, expected `= 5`
- **PASS** `coverage_prerequisite` — actual `5`, expected `= 5`
- **PASS** `coverage_multi_hop` — actual `5`, expected `= 5`
- **PASS** `adaptive_p95_within_budget` — actual `251.3`, expected `<= 500 ms`
- **PASS** `adaptive_direct_no_material_regression` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `adaptive_prerequisite_no_regression` — actual `0.0`, expected `>= 0 recall delta`
- **PASS** `adaptive_multi_hop_no_regression` — actual `0.0`, expected `>= 0 recall delta`
