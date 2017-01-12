from xml.dom import minidom

doc = minidom.parse("config.xml")

slaves = doc.getElementsByTagName("slave")
for slave in slaves:
        name = slave.getElementsByTagName("name")[0].firstChild.data
#        print name
        tools = slave.getElementsByTagName("hudson.tools.ToolLocationNodeProperty_-ToolLocation")
        for tool in tools:
        	tool_name = tool.getElementsByTagName("name")[0].firstChild.data
        	tool_home = tool.getElementsByTagName("home")[0].firstChild.data

        	if tool_name == "JDK_1.7.0_LATEST" and tool_home == "/gf-hudson-tools/jdk/7/jdk1.7.0_09":
        		print name

        
