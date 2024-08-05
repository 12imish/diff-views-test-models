project 2.0
modelVersion 5
parent

artifactId base
version 1.6.0

artifactId simulink-model-extension
version 0.5.0-SNAPSHOT
packaging pom
properties
worker.version 0.55.0

scm
connection scm:git:git@github.mathworks.com:development/simulink-model-extension.git
developerConnection scm:git:git@github.mathworks.com:development/simulink-model-extension.git
build

worker-matlab.version 0.29.0
distributionManagement
site
id doc_website
name MathWorks Maven Project Docs
url file:/mathworks/inside/files/dev/tools/maven_sites/dc/simulink-model-extension/versions/${project.version}/
modules
module
matlab-scripts