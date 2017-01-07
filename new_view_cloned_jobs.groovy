import hudson.model.*
 
def oldview = "Trunk Continuous"
newview = "4.1.2"
str_search = "trunk"
str_replace = "4.1.2"
 
def view = Hudson.instance.getView(oldview)
def view_new = Hudson.instance.getView(newview)
 
//copy all projects of a view
for(item in view.getItems())
{

  //create the new project name
  newName = item.getName().replace(str_search, str_replace)
 
  // copy the job, disable and save it
  def job = Hudson.instance.copy(item, newName)
  view_new.add(job)
 
  println(" $item.name copied as $newName")

}
