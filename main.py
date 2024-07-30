import os
package_directory = os.path.dirname(os.path.abspath(__file__))
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().split('\n')

testcases = read_file(os.path.join(package_directory, 'testcases.txt'))
answer = read_file(os.path.join(package_directory, 'answer.txt'))
output = read_file(os.path.join(package_directory, 'output.txt'))
del testcases[0]
linesPerTestcase = int(input('Lines per testcase: '))
linesPerOutput = int(input('Lines per output: '))
found = False
print('---------------\n')
for i in range(len(testcases) // linesPerTestcase):

    if (i*linesPerTestcase > len(testcases) or i*linesPerOutput >= min(len(output), len(answer))):
        break
    testcase = "\n".join(testcases[x] for x in range(i*linesPerTestcase, linesPerTestcase * (i+1)))
    local_answer =  "\n".join(answer[x] for x in range(i*linesPerOutput, linesPerOutput * (i+1)))
    local_output =  "\n".join(output[x] for x in range(i*linesPerOutput, linesPerOutput * (i+1)))
    if (local_answer.upper() != local_output.upper()):
        found = True
        print("Testcase " + str(i+1) + " failed")
        print(testcase)
        print("Expected: ", local_answer)
        print("Received: ", local_output)
        print('\n---------------\n')
if not found:
    print("Hurray! No wrong answers")

