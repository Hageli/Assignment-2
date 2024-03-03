from xmlrpc.server import SimpleXMLRPCServer
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

def add_note(user_topic, note_name, user_text, timestamp):
    tree = etree.parse("db.xml")
    root = tree.getroot()

    if(user_topic == ""):
        return "Note topic cannot be empty"
    elif(note_name == ""):
        return "Note name cannot be empty"
    elif(user_text == ""):
         return "Note text cannot be empty"

    for topic in tree.findall('topic'):
        if(topic.attrib['name'] == user_topic):
            new_note = etree.SubElement(topic, 'note')
            new_note.set('name', note_name)
            new_text = etree.SubElement(new_note, 'text')
            new_text.text = user_text
            new_timestamp = etree.SubElement(new_note, 'timestamp')
            new_timestamp.text = timestamp
            etree.indent(root, space="    ")
            tree.write("db.xml", pretty_print=True)
            return "Note added"

    new_topic = etree.SubElement(root, 'topic')
    new_topic.set('name', user_topic)
    new_note = etree.SubElement(new_topic, 'note')
    new_note.set('name', note_name)
    new_text = etree.SubElement(new_note, 'text')
    new_text.text = user_text
    new_timestamp = etree.SubElement(new_note, 'timestamp')
    new_timestamp.text = timestamp
    etree.indent(root, space="    ")
    tree.write("db.xml", encoding='UTF-8', pretty_print=True)
    return "Note added"


def read_xml(user_topic):
    tree = etree.parse("db.xml")
    return_array = []
    for topic in tree.findall('topic'):
        if(topic.attrib['name'] == user_topic):
            for note in topic.findall('note'):
                return_array.append([note.attrib['name'], note[0].text, note[1].text])
            return return_array
    return "Not Found"

# Setting up the server and functions
server =  SimpleXMLRPCServer(('localhost', 3000))
server.register_function(add_note, "add_note")
server.register_function(read_xml, "read_xml")
server.serve_forever()