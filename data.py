import string
w = '''Do you speak English Hello Good Morning Good afternoon Good evening Welcome
 Goodbye
 Please
 Thank you
I’m sorry  Please excuse me
Do you know how to get to Can you show me how to get to
Please write that down for me
I am allergic to I need a doctor
 I am an Citizen I am looking for the Embassy 
 I have blood type
 I need help
 I’m lost
 Please call the police I need a doctor
common = set()
for words in w.splitlines():
    for i in words.split(" "):
        if i.isdigit():
            continue
        else:
            common.add(i)
print(common)
ASL = ['feel', 'happy', 'sad', 'angry', 'hi', 'project', 'our', 'we', 'translate', 'speech', 'enjoy', 'hope', 'society','you', 'deaf','mute', 'ASL', 'sorry', 'excuse me', 'food', 'water', 'name', 'friend', 'my', 'when', 'where', 'which', 'who', 'yes' , 'no', 'tired', 'am', 'call', 'excuse', 'an', 'looking', 'I', 'blood', 'type', 'get', 'Do', 'speak', 'evening', 'Hello', 'Please', 'afternoon', 'Can', 'police', 'Citizen', 'Morning', 'Welcome', 'I’m', 'lost', 'to', 'Thanks', 'sorry', 'allergic', 'Embassy', 'me', 'have', 'doctor', 'help', 'down', 'Goodbye', 'show', 'Good', 'how', 'know', 'write', 'English', 'need']
ASL = [word.lower() for word in ASL]
ASL = sorted(ASL)
print(ASL), , 'embassy', 
'english', 'enjoy', 'evening','excuse', 'excuse me', 'feel', 'food', 'friend', 'get', 'good', 'goodbye', 'happy', 'have', 'hello', 
'help', 'hi', 'hope', 'how', 'i', 'i’m', 'know', 'looking', 'lost', 'me', 'morning', 'mute', 'my', 'name', 'need', 'no', 'our', 'please', 'police', 'project', 'sad', 'show', 'society', 'sorry', 'sorry', 'speak', 'speech', 'thanks', 'tired', 'to', 'translate', 'type', 'water', 'we', 'welcome', 'when', 'where', 'which', 'who', 'write', 'yes', 'you']''' 
''''''


labels = ['afternoon', 'allergic', 'angry', 'asl', 'blood', 'call', 'can', 'deaf', 'doctor', 'down', 'Hi', 'Our', 'Speech', 'A', 'S','L', 'project', 'enjoy']

l = []
num = 1
for i in range(len(labels)):
    temp = {}
    temp['name'] = labels[i]
    temp['id'] = i + 1
    l.append(temp)
print(l)

