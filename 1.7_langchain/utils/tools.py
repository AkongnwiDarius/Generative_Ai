from langchain_core.tools import tool

@tool
def get_module_deadline(module_name:str) -> str:
    """ Look up the submission deadline for a named bootcamp
    
    Args:
        module_name: the modele name e.g., 'ANN','CNN','LLM'
    """
    deadline = {
        'ANN':'2026-09-16',
        'CNN':'2026-09-17',
        'LLM':'2026-09-23'
    }

    return deadline.get(module_name, 'No deadline found for that module')



@tool
def count_students_in_module(module_name:str) -> str:
    """Look up how many students are enrolled in a named bootcamp module"""

    counts = {'ANN': 24, 'CNN': 21, 'LLM': 34}
    return str(counts.get(module_name, 0))

# """ docstring is the description of what the tool is all about, its very vey importantbecause models what the tool is all about"""
