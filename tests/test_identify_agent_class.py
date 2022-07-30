from hachess.common import identify_agent_class, hachess_local_directory


def test_iac():
    hld = hachess_local_directory()
    assert identify_agent_class(f"{hld}/agents/template") == "Agent"
    assert identify_agent_class(f"{hld}/agents/Adam_SimpleMiniMax") == "Agent"


if __name__ == "__main__":
    test_iac()
