from langchain_core.tools import tool

#tool for looking up submission deadline for a named module
@tool
def module_deadline_lookup(module_name:str) -> str:
    """look up the submission deadline for a named course
    Args:
        course_name: the name of the course eg 'Computer Architechture','Statistics','Engineering Drawing'
        
    """
    deadlines = {
        'Computer Architechture': '2026-09-16',
        'Statistics': '2026-10-17',
        'Engineering Drawing': '2026-11-23'
    }

    return deadlines.get(module_name, 'No deadline found for that course')

#tool for counting students in a module
@tool
def student_count_lookup(module_name:str) -> int:
    'look up how many students are enrolled in a named module'
    counts = {'Computer Architechture':55, 'Statistics': 77, 'Engineering Drawing': 42}
    return counts.get(module_name, 'students not found') 

#which tool must be completed before which
@tool
def prerequisite(tool_name:int) -> int:
    'look up which tool must be completed before which'
    prerequisities = {
        'Computer Architechture': '1',
        'Statistics':'2',
        'Engineering Drawing':'3'
    }
    return prerequisities.get(tool_name, 'prerequisite not found')

#session for a specific named module
@tool
def session_module_lookup(module_name:str) -> str:
    'Look up the room and schedule for a specific named module'
    session = {
        'Computer Architechture': 'Amphi 350',
        'Statistics': 'Asanji Hall 1',
        'Engineering Drawing': 'CCAST Room 12'
    }
    return session.get(module_name, 'session not found')


