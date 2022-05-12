from PatchNote import PatchNote

n_tests = 2

print(f"Starting tests for langs {PatchNote.langs} for last {n_tests} patchs...")

tests_passed = []
tests_failed = []

for lang in PatchNote.langs:
    for i in range(n_tests):
        try:
            tests_passed.append((lang,i,PatchNote(previous = i, lang = lang)))
            print(f"Test for lang = '{lang}', previous = '{i}' passed.")
        except Exception as err:
            print(f"Test for lang = '{lang}', previous = '{i}' failed with error: '{type(err)}'")
            tests_failed.append((lang,i,err))
    
n_tests_total = n_tests*len(langs)
n_tests_passed_total = len(tests_passed)
print("|"+"-"*80)
print("|"+"-"*80)
print(f"| {int(n_tests_passed_total*100/n_tests_total)}% of success.")
print("|"+"-"*80)



for i in range(len(tests_passed)):
    input("| Press a key to see the next passed tests...")
    test = tests_passed[i]
    print("|"+"-"*80)
    print("|"+"-"*80)
    print(f"| Patch for lang = '{test[0]}', previous = '{test[1]}'")
    print("|"+"-"*80)
    print(test[2])
    print("|"+"-"*80)
    print("|"+"-"*80)
    
    


