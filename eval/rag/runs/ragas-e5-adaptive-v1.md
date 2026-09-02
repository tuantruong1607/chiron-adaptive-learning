# Chiron RAGAS retrieval baseline

- Dataset: `eval\rag\golden.jsonl`
- Cases: **50**
- Collection: `chiron_chunks_v1`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **FAIL**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| dense | 0.820 | 0.590 | 0.540 | 0.429 | 0.132 | 0.590 | 248.3 |
| bm25 | 0.820 | 0.460 | 0.489 | 0.359 | 0.117 | 0.460 | 239.5 |
| hybrid | 0.880 | 0.617 | 0.566 | 0.440 | 0.139 | 0.617 | 281.5 |
| adaptive | 0.840 | 0.567 | 0.400 | 0.367 | 0.150 | 0.567 | 979.3 |

## By query class

### dense

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 20 | 1.000 | 0.950 | 0.807 | 0.687 |
| prerequisite | 15 | 0.667 | 0.300 | 0.325 | 0.223 |
| multi_hop | 15 | 0.733 | 0.400 | 0.400 | 0.291 |

### bm25

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 20 | 0.950 | 0.750 | 0.550 | 0.481 |
| prerequisite | 15 | 0.667 | 0.233 | 0.428 | 0.263 |
| multi_hop | 15 | 0.800 | 0.300 | 0.469 | 0.293 |

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 20 | 1.000 | 0.950 | 0.728 | 0.635 |
| prerequisite | 15 | 0.800 | 0.433 | 0.414 | 0.293 |
| multi_hop | 15 | 0.800 | 0.356 | 0.502 | 0.328 |

### adaptive

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 20 | 1.000 | 0.900 | 0.703 | 0.612 |
| prerequisite | 15 | 0.667 | 0.333 | 0.162 | 0.168 |
| multi_hop | 15 | 0.800 | 0.356 | 0.234 | 0.240 |

## Largest adaptive recall regressions

| Case | Class | Hybrid recall | Adaptive recall | Delta |
| --- | --- | ---: | ---: | ---: |
| ret-001 | direct | 1.000 | 0.000 | -1.000 |
| ret-009 | prerequisite | 0.500 | 0.000 | -0.500 |
| ret-033 | prerequisite | 1.000 | 0.500 | -0.500 |
| ret-034 | prerequisite | 0.500 | 0.000 | -0.500 |
| ret-015 | multi_hop | 1.000 | 0.667 | -0.333 |
| ret-014 | prerequisite | 0.000 | 0.000 | +0.000 |
| ret-006 | direct | 1.000 | 1.000 | +0.000 |
| ret-018 | multi_hop | 0.000 | 0.000 | +0.000 |
| ret-020 | multi_hop | 0.333 | 0.333 | +0.000 |
| ret-027 | direct | 1.000 | 1.000 | +0.000 |

## Quality gates

- **PASS** `dataset_has_50_cases` — actual `50`, expected `>= 50`
- **PASS** `all_cases_human_approved` — actual `50`, expected `= 50`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `50`, expected `= 50`
- **PASS** `coverage_direct` — actual `20`, expected `>= 20`
- **PASS** `coverage_prerequisite` — actual `15`, expected `>= 15`
- **PASS** `coverage_multi_hop` — actual `15`, expected `>= 15`
- **FAIL** `adaptive_direct_no_material_regression` — actual `-0.05`, expected `>= -0.02 recall delta`
- **FAIL** `adaptive_prerequisite_no_regression` — actual `-0.1`, expected `>= 0 recall delta`
- **PASS** `adaptive_multi_hop_no_regression` — actual `0.0`, expected `>= 0 recall delta`
