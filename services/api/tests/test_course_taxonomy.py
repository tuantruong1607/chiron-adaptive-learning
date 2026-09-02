from collections import Counter

from app.question_bank import _NODES_BY_ID, _TAXONOMY, _concept_for_topic
from app.learning_resources import resources_for_concepts
from app.seed import QUESTIONS
from app.seed import CONCEPTS


def test_every_question_bank_topic_maps_to_a_published_taxonomy_node() -> None:
    mapped = {
        topic
        for node in _TAXONOMY["nodes"]
        for topic in node.get("question_topics", [])
    }
    from app.question_bank import _BANK

    assert {item["topic"] for item in _BANK} == mapped
    assert all(_concept_for_topic(item["topic"]) in _NODES_BY_ID for item in _BANK)


def test_diagnostic_has_25_questions_and_covers_the_whole_course() -> None:
    assert len(QUESTIONS) == 25
    assert len({question.id for question, _ in QUESTIONS}) == 25
    domains = Counter(
        _NODES_BY_ID[question.concept_id]["domain"] for question, _ in QUESTIONS
    )
    assert set(domains) == {domain["id"] for domain in _TAXONOMY["domains"]}
    assert domains["foundations_product"] == 5
    assert max(domains.values()) <= 5


def test_full_course_taxonomy_has_no_isolated_nodes_or_broken_edges() -> None:
    nodes = {node["id"] for node in _TAXONOMY["nodes"]}
    degree = Counter(
        endpoint
        for edge in _TAXONOMY["edges"]
        for endpoint in (edge["source"], edge["target"])
    )
    assert len(nodes) >= 60
    assert len(_TAXONOMY["edges"]) >= len(nodes)
    assert all(edge["source"] in nodes and edge["target"] in nodes for edge in _TAXONOMY["edges"])
    assert not (nodes - set(degree))


def test_every_knowledge_node_opens_a_grounded_learning_resource() -> None:
    resources = resources_for_concepts(CONCEPTS)
    assert {resource.concept_id for resource in resources} == {
        concept.id for concept in CONCEPTS
    }
    assert all(resource.citations for resource in resources)
    assert all(resource.learning_outcome for resource in resources)
