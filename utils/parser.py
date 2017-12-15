from reader import get_test

# Key = Language. Value = Action
# Check for the given language string in the step, and if it contains that string
# It assigns it the appropriate action

language_action = {

    "login": "login",
    "logout": "logout",
    "click on ": "click_",
    "collapse sidebar": "sidebar_hamburger",
    "expand sidebar": "sidebar_hamburger",
    "go to ": "sidebar_",
    "choose ": "choose_",
    "lands on webpage": "open_kibopush"
}



def get_action(step):
    step = step.lower()
    action = "Not Defined"
    # To check for ambiguity, whether one step is translated to multiple action
    repeat = 0
    # print language_action.keys()
    for language in language_action.keys():
        if language in step:
            action = language_action[language]
            repeat = repeat + 1
        if repeat > 1:
            action = "Ambigous"
    return action

def criteria(test):
    errors = ['Ambigous', 'Not Defined']
    for error in errors:
        if test[-1] == error:
            return False
    return True

def remove_incomplete(all_test):
    pruned_list = [x for x in all_test if criteria(x)]
    return pruned_list


def parse_language():

    all_test = get_test()
    unparsable = []
    ambigous = []
    test_actions = []
    test_case = []
    not_parsed = 0

    for case in all_test:
        for step in case:
            if step == '':
                continue
            action = get_action(step)
            test_actions.append(action)
            if action == "Not Defined":
                unparsable.append(step)
                not_parsed = not_parsed + 1
                break
            elif action == "Ambigous":
                ambigous.append(step)
                not_parsed = not_parsed + 1
                break
        test_case.append(test_actions)
        test_actions = []

    print("Total Cases : ", len(all_test))
    print("Not Parsed : ", not_parsed)
    print("Ambigous:", ambigous)

    pruned_test = remove_incomplete(test_case)

    print("Length of Pruned Test: ", len(pruned_test))

if __name__ == '__main__':
	parse_language()