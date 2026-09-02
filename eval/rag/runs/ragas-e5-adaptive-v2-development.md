# Chiron RAGAS retrieval baseline

- Dataset: `eval\rag\golden.jsonl`
- Cases: **35**
- Collection: `chiron_chunks_v1`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **PASS**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| dense | 0.829 | 0.600 | 0.540 | 0.436 | 0.129 | 0.600 | 236.5 |
| bm25 | 0.829 | 0.524 | 0.502 | 0.373 | 0.116 | 0.524 | 216.2 |
| hybrid | 0.886 | 0.624 | 0.587 | 0.444 | 0.127 | 0.624 | 242.3 |
| adaptive | 0.886 | 0.633 | 0.584 | 0.446 | 0.129 | 0.633 | 299.6 |

## By query class

### dense

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 1.000 | 0.933 | 0.820 | 0.674 |
| prerequisite | 10 | 0.600 | 0.250 | 0.284 | 0.202 |
| multi_hop | 10 | 0.800 | 0.450 | 0.374 | 0.312 |

### bm25

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 0.933 | 0.867 | 0.592 | 0.510 |
| prerequisite | 10 | 0.700 | 0.200 | 0.467 | 0.266 |
| multi_hop | 10 | 0.800 | 0.333 | 0.403 | 0.276 |

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 1.000 | 0.933 | 0.802 | 0.650 |
| prerequisite | 10 | 0.800 | 0.400 | 0.383 | 0.268 |
| multi_hop | 10 | 0.800 | 0.383 | 0.470 | 0.312 |

### adaptive

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 15 | 1.000 | 0.933 | 0.802 | 0.650 |
| prerequisite | 10 | 0.800 | 0.400 | 0.379 | 0.266 |
| multi_hop | 10 | 0.800 | 0.417 | 0.462 | 0.321 |

## Largest adaptive recall regressions

| Case | Class | Hybrid recall | Adaptive recall | Delta |
| --- | --- | ---: | ---: | ---: |
| ret-041 | prerequisite | 0.000 | 0.000 | +0.000 |
| ret-012 | prerequisite | 0.000 | 0.000 | +0.000 |
| ret-024 | direct | 1.000 | 1.000 | +0.000 |
| ret-022 | direct | 1.000 | 1.000 | +0.000 |
| ret-017 | multi_hop | 0.667 | 0.667 | +0.000 |
| ret-010 | prerequisite | 0.000 | 0.000 | +0.000 |
| ret-003 | direct | 1.000 | 1.000 | +0.000 |
| ret-025 | direct | 1.000 | 1.000 | +0.000 |
| ret-049 | multi_hop | 0.000 | 0.000 | +0.000 |
| ret-006 | direct | 1.000 | 1.000 | +0.000 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `35`, expected `= 35`
- **PASS** `all_cases_human_approved` — actual `35`, expected `= 35`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `35`, expected `= 35`
- **PASS** `coverage_direct` — actual `15`, expected `= 15`
- **PASS** `coverage_prerequisite` — actual `10`, expected `= 10`
- **PASS** `coverage_multi_hop` — actual `10`, expected `= 10`
- **PASS** `adaptive_p95_within_budget` — actual `299.6`, expected `<= 500 ms`
- **PASS** `adaptive_direct_no_material_regression` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `adaptive_prerequisite_no_regression` — actual `0.0`, expected `>= 0 recall delta`
- **PASS** `adaptive_multi_hop_no_regression` — actual `0.0333`, expected `>= 0 recall delta`
