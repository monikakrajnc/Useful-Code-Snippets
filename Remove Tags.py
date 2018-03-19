# remove_tags takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.



def remove_tags(strings):
    n = len(strings)
    list = []
    c = 0
    if strings.find(">") == - 1 and n > 0:          #if there aren't any '>', means there are just words
        list = strings.split()
        return list
    else:
        while c < n:
            a = strings.find(">", c)              #find first '>' and then find '<', which is after '>'
            b = strings.find("<", a)              #between these two signs is word
            word = str(strings[a+1 : b])
            if word.find(" ") == -1:              #if there is no empty space, it means it is just one word
                list.append(word)
            else:
                word = word.split()               #if there is and empty space, make a split on that position
                list = list + word
            c = a + 1
    for i in list:          #if the first or last element in the list is an empty space, remove it
        if len(i) == 0:
            list.remove(i)
    if len(list[-1]) == 0:
        list.pop()
    return list     #the list of words

#or as in the video:


def remove_tags(strings):
	a = strings.find("<")
	while a != - 1:
		b = strings.find(">", a)
		strings = strings[ :a] + " " + strings[b + 1 : ]
		a = strings.find("<")
	return strings.split()


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']
