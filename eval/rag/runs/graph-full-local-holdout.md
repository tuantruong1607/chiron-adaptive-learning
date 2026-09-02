# Chiron RAGAS retrieval baseline

- Dataset: `/workspace/eval/rag/golden-local.jsonl`
- Cases: **15**
- Collection: `chiron_chunks_v1_full`
- Embedding: `intfloat/multilingual-e5-large` / `multilingual-e5-large-mean-batch32-v2`
- RAGAS: `0.4.3`
- Quality gate: **FAIL**

## Overall

| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hybrid | 0.400 | 0.144 | 0.248 | 0.183 | 0.073 | 0.144 | 436.3 |
| graph_lite | 0.400 | 0.144 | 0.248 | 0.183 | 0.073 | 0.144 | 633.2 |

## By query class

### hybrid

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 0.400 | 0.200 | 0.250 | 0.222 |
| prerequisite | 5 | 0.200 | 0.100 | 0.029 | 0.060 |
| multi_hop | 5 | 0.600 | 0.133 | 0.467 | 0.268 |

### graph_lite

| Class | Cases | Hit@K | Required recall | MRR | nDCG |
| --- | ---: | ---: | ---: | ---: | ---: |
| direct | 5 | 0.400 | 0.200 | 0.250 | 0.222 |
| prerequisite | 5 | 0.200 | 0.100 | 0.029 | 0.060 |
| multi_hop | 5 | 0.600 | 0.133 | 0.467 | 0.268 |

## Quality gates

- **PASS** `dataset_has_expected_cases` — actual `15`, expected `= 15`
- **PASS** `all_cases_have_resolved_source_labels` — actual `15`, expected `= 15`
- **PASS** `retrieval_suite_contains_only_user_questions` — actual `15`, expected `= 15`
- **PASS** `coverage_direct` — actual `5`, expected `= 5`
- **PASS** `coverage_prerequisite` — actual `5`, expected `= 5`
- **PASS** `coverage_multi_hop` — actual `5`, expected `= 5`
- **FAIL** `graph_lite_p95_within_budget` — actual `633.2`, expected `<= 500 ms`
- **PASS** `graph_lite_direct_recall_gate` — actual `0.0`, expected `>= -0.02 recall delta`
- **PASS** `graph_lite_prerequisite_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
- **PASS** `graph_lite_multi_hop_recall_gate` — actual `0.0`, expected `>= 0 recall delta`
