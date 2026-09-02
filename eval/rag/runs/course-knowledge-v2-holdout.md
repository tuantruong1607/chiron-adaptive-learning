# Chiron RAGAS retrieval baseline

- Dataset: `eval/rag/golden-local.jsonl`
- Cases: **15**
- Collection: `chiron_chunks_v1_full`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **PASS**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | 0.467 | 0.167 | 0.248 | 0.199 | 0.087 | 0.167 | 335.4 |
| graph_lite | 0.467 | 0.167 | 0.248 | 0.199 | 0.087 | 0.167 | 324.7 |

## By query class

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 0.600 | 0.200 | 0.283 | 0.255 |
| prerequisite | 5 | 0.200 | 0.100 | 0.029 | 0.058 |
| multi_hop | 5 | 0.600 | 0.200 | 0.433 | 0.283 |

### graph_lite

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 0.600 | 0.200 | 0.283 | 0.255 |
| prerequisite | 5 | 0.200 | 0.100 | 0.029 | 0.058 |
| multi_hop | 5 | 0.600 | 0.200 | 0.433 | 0.283 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `15`, expected `= 15`
- **PASS** `all_cases_have_resolved_source_labels` — actual `15`, expected `= 15`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `15`, expected `= 15`
- **PASS** `coverage_direct` — actual `5`, expected `= 5`
- **PASS** `coverage_prerequisite` — actual `5`, expected `= 5`
- **PASS** `coverage_multi_hop` — actual `5`, expected `= 5`
- **PASS** `graph_lite_p95_within_budget` — actual `324.7`, expected `<= 500 ms`
- **PASS** `graph_lite_direct_recall_gate` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `graph_lite_prerequisite_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
- **PASS** `graph_lite_multi_hop_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
