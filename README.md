## AZURE + docker
* Create a container registry(Create resource group if needed
  * after container registry created, go to access keys and enable admin
  * also save the login server and password
* Build docker image(when login, use ur username and password above):
  ```
  docker build -t <login server URL>/<name your application>:latest .
  docker login <login server URL>
  docker push <login server URL>/<application name>:latest
  ```
*  create web app
  * publish: container
  * free deplyoment option
  * container page:
    * image source:azure container registry
    * it should add your image you created above
  * everything else default
* In your webapp, go to deployment center
  * set continous deplyoment to on
  * Then in source, go to github actions
    * put your github stuff in there and set the correct values
   
  FInished
    
   
