# Resources

    @peterrenshaw @tyabblemons Once such links are discovered and 
    put into linkable notebooks, can be shared out to other SMEM. [0]

There is a need for resources (such as URLs) to be stored somewhere so they can be used
as a *"trusted resource"*. This of course implies that the data store is up to date and 
valid and distributable.

One possible solution is to create a list of URLs that are required storing some metadata
along with the link. While humans will ultimately use this data, why would you want to 
store the data in a machine readable/distributable format?

### Storage

    Store machine readable, export to human readable form.

For reasons of accuracy it is desirable to store information once and only once. There should 
be a master list. If this list is in a machine readable format, it is possible to do the following
desirable things:

* automatic verification
  - test for link rot
  - act as link to new url

* ability to generate a customisable human readable format (formats)
  - txt
  - html
  - text description + minimised url?

* add additional metadata to the information
  - description of resource
  - revision information
  - who added the data
  - last updated
  - verification history
  - correction history

* OSOM (one source, one message)
  - one version of the information that is correct


### Metadata

    Store the history and description of data

The ability to capture more than just the actual data. 


### Resource types

    The type of resource will determine how it should be stored. Structured resources
    might benifit a machine readable data format. Unstructured may benifit more from a 
    WIKI.

Resources should not be restricted to just web URLs. It could be anything from contact information to
procedures that might be followed. For unstructured information a **Wiki** might be suitable. So care must
be taken choosing how resources are stored depending on the use. 


### Access

    If the admin gets run over by a bus, how do you fix things?

Needs to be assigned to a particular person or persons and has to be verifiable. Some mechanism to make
changes independent of owner. cf: bus scenario [1]


### Distribution

    You do not want this to disappear or be unavailable when most needed.

Key point. No use having the data in a place that cannot withstand the slashdot effect. No use having
the data locked up in a database that can fall over. Simple is better. Human and macine 
readable formats, is best. 


## Resources

[0] [@geehall1](https://twitter.com/geehall1)
<https://twitter.com/geehall1/status/364298994391842817>

[1] The bus scenario is where one person is responsible for something and a bus runs them over. How do 
you handle this?

vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
