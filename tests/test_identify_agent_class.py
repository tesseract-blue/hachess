from hachess.common import identify_agent_class


def test_iac():
    assert identify_agent_class("../hachess/agents/template") == "Agent"
    assert identify_agent_class("../hachess/agents/Adam_SimpleMiniMax") == "Agent"
