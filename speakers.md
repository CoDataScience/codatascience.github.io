---
layout: default
title: Home
---
<h1>Speakers</h1>


#### Meet a Data Scientist Series

* Every week, we begin our team meeting by hearing from a practicing data scientist or data science researcher.<
* Usually 5 to 15 minutes long, these talks provide Colorado Data Science Team members an idea of what data science looks like in practice, beyond classroom projects and competitions.
* Researchers often share what techniques they are developing, or how they use existing techniques to advance scientific knowledge or engineering practice; practicing data scientists in industry often share the techniques and algorithms that they find to be most useful in their work, and their experiences about what works and when it works.
* Aside from keeping team members informed about their options after they graduate from CU, these talks also foster relationships with local data scientists which we hope will continue to grow.

If you are a data scientist (broadly construed) and believe a presentation on your current work would be a good fit for the Colorado Data Science Team, please reach out to the leadership team at codata@colorado.edu


<div class="pull-left">
{% for speaker in site.speakers %}
	<div class="panel panel-default">
		<div class="panel-heading">
			<h3> <a href="{{speaker.website}}"> {{speaker.speaker}} </a></h3> 
			<h4> {{ speaker.position }} </h4>
			<h5> <a href="/{{ speaker.posturl }}"> Link to Post</a> </h5>
		</div>
		<div class="panel-body">
   			<img alt="{{ speaker.speaker }}" src="/images/speakers/{{speaker.image}}" style="height:100px;width:100px" 	class="thumbnail col-md-4">
   			<div class="col-md-8">{{ speaker.output }}</div>
   		</div>
   	</div>
{% endfor %}
</div>