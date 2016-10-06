---
layout: default
title: Home
---
<h1>Speakers</h1>



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
