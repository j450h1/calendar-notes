* [Interactive Data Visualization with D3.js](http://chimera.labs.oreilly.com/books/1230000000345/index.html): Finished Chapter 3 (Technology Fundamentals) and Chapter 4 (Setup).

	* **Chapter 3: Technology Fundamentals**: I love this chapter. Here are the basic ideas:

		* **The web**: Cover the concept of conversations between Server (either remote or localhost) and Client (often Browsers). The client requests for information, the server return with response. 

		* **URL**: Protocol + URI + port + subpages

		* **HTML**:
			* **Content + Structure**: Like Markdown is used for visual structure, HTML is used to specify semantic structure (attaching hierarchy, relationships, and meaning to the contents)
			* **Adding structure with elements + common element**: html, head (where css, .js, script are placed), title, body, h1/2/3/4, p, ul, ol, li...etc.
			* **Attributes, classes, and IDs** (only unique in a single page)
			* **DOM**: Document Object Model refers to the hierarchical structure of HTML. After the client receives the HTML raw text, we will need to translate it into a DOM.
			* **Developer Tool**: Mainly focus on Google chrome (Command + Option + I)
			* **Rendering**: the process by which browsers, after parsing HTML and generating DOM, apply visual rules to the DOM content.

				* **CSS**: the concept of selectors -> properties and values. Call cascading because enforcement is done in cascading style (top-bottom), but really it's driven by specificity (i.e. how specific the rule is)
				* **How to use CSS on HTML**:
					* Embedded CSS in your HTML
					* Reference an external stylesheet from HTML
					* Attach inline styles (not recommended)
				* Inheritance, Cascading, and Specificity

		* **Javascript**:

			* Variable, arrays, and javascript objects
			* JSON, which is a specific type of javascript object
			* Mathematical operations, comparison operators
			* Control structure 
			* Functions

			* Referencing Scripts
				* Include directly in HTML
				* Reference in a separate .js file

			* Javascript Gotchas!
				* Dynamic typing. Javascript is not a strongly typed language like Java
				* Variable hoisting (don't really get this)
				* Function level-scope
				* Global namespace
		
		* **SVG**:
			* The SVG element
			* Styling SVG element in CSS
			* Layering and drawing orders
			* Transparancy
	
	*  **Chapter 4**: I also successfully setup the environment. The steps are simple
		* mkdir d3-project-folder
		* mkdir d3-project-folder/d3
		* touch d3-project-folder/index.html
		* git clone d3 repo and place d3.js in d3-project-folder
		* In d3-project-folder, at command line, type: python -m SimpleHTTPServer 8888 &.

* [Interactive Data Visualization with D3.js: Chapter 5](http://chimera.labs.oreilly.com/books/1230000000345/index.html): Finished Chapter 5 (data)
	* Introduce the concept of *chaining* (d3 methods)
	* Binding data, how to do it?
		* First, load the data
			* Loading .csv, .tsv, or .json are all very similar. Use the _d3.csv_, _d3.tsv_, or _d3.json_
			* They all have the same form _d3.filetype("filename.filetype", callback function)_
			* Pay particular attention to the "Handling data loading errors" because it explains:
				* how _d3.csv_ loading methods are asynchronous
				* how the callback function will not be called until data is (successfully) loaded so referencing the data outside of the callback will give error
				* how the callback function will still be called after even if data failed to load and need error handling to catch those
		* Bind the data ("Please make your selection" section)
			* _ds.select.data.enter_ pattern.
				* You first **select** the DOM elements
				* You then bind the selected DOM elements with **data**
				* You then **enter** the data into the HTML
				* and do whatever additional mainpulation you need to display the content
	* Why we always wrap _function(d)_ inside a d3.{text,attribute}... method?
		* "data wants to be held" section: we need to hug data **d** in an anonymous function.

* [Interactive Data Visualization with D3.js: Chapter 6](http://chimera.labs.oreilly.com/books/1230000000345/ch06.html): 
From the previous chapter, we learn about:
	* Chaining d3 methods
	* Loading data into d3.js so we can manipulate them
	* How to map data to visuals (this is the essence of data viz) using anonymous function

We didn't really draw anything specific, and in chapter 6, we see how to draw bar charts, scatterplot in SVG form. Finished Chapter 6 (Drawing with data)

* **Drawing div**
	* we learn about the functionalities of _attr_, _style_. The basic idea is to map each datum to visual elements:
		* _attr_ sets an HTML attribute and its value on an element. An HTML attribute is any porperty/value pair that you could include between an element's \<\> brackets.
		* _styel_ applies CSS style directly to an element. This is the equivalent of including CSS rules within a style attribute right in your HTMLs
	* The use of anonymous function is once again emphasized.

* **The power of data**
	* Again, this section emphasize the fact that binding data to DOM element is the essence of data viz in d3.js.

* **Drawing SVGs:**
In this section, we will be operating on SVGs. I think the lessons learned for me is that the HTML structure will be body/SVG/{SVG element1, SVG element2 ...etc}. The SVG layer is between body and SVG elements, and it provides the "canvas" for the elements to be displayed. The best way to see this is to follow the chapter 6 example, and see the resulting HTML page to see the structure.
	
	* create a svg: _svg = d3.select("body").append("svg").attr("width", w).attr("height", h)_. We often create the svg variable, because this particular chaining method will return a pointer/reference to the actual svg object. Saving it in a variable is convenient because we don't have to refer them in the chain the next time we need to use it.
	
	* The next step is then incude SVG elements in the SVG layer: _svg.selectAll("circle").data(dataset).enter().append("circle")_
	
	* Finally, once the data is binded, we map the data with HTML attributes using attr.

* **Drawing SVG bar chart**:
In here, we replicate the same drawing of a bar chart, but now in SVG form. Quick lessons:
	* Be aware of the reference x,y coordinates. They are on the upper-left.
	* Spacing is also important. We also want to make sure things don't go out of bound. We will learn _scale()_ soon
	* If you would like to avoid using _.attr()_ multiple times, you could use [multivalue maps](http://bl.ocks.org/mbostock/3305515)
	* We also learn how to add labels

* **Drawing scatterplot**: 
	* The process is very similar as above, the additional thing here is the data we load in is an array of array. To reference the data, we need to use the dataset[5][1] or datum[0] syntax.

* [Interactive Data Visualization with D3.js: Chapter 7](http://chimera.labs.oreilly.com/books/1230000000345/ch07.html):
	
	* "Scales are functions that map from an input domain to an output range" -- Mike Bostock
	
	* We will introduce only the linear scale in this chapter. See the end of the chapter for more scales. Same ideas though.
	
	* The main use cases for scale of course is that you can map the values of the data to the scale of the visual pan you have, and you never had to worry about doing the math yourself to figure out the scale transformation.
	
	* With **linear scale**, all it does it normalization:
		* The input value is normalized to a number between 0 and 1, according to the domain
		* and then the normalized value is scaled to the output range.
	
	* **Creating a scale**:
		* _var scale = d3.scale.linear()
						.domain([100, 500])
						.range([10, 350])_
		* Then you can start using the scale function like _scale(100)_
	
	* *min & max* function:
		* Very handy, _d3.max(dataset, anon function)_, where the anon function is often a **accessor** to get an datum from a more complicated data structure (e.g. getting the first element of an array [x1, x2])
		* The min and max function are often used in the _.domain()_ and _.range()_ function

	* Once you have the scale function, you can start applying them in places where you input the data value. e.g. d[1] -> xScale(d[1])

	* To reverse the vertical orientation, simply replace _.range[0, h]_ with _.range([h, 0])_

	* Padding is another concern we should take care off. This chapter does it in a ad-hoc way, to learn more systematic approach, see [**Mike Bostock's margin convention**](http://bl.ocks.org/mbostock/3019563)

* [Interactive Data Visualization with D3.js: Chapter 8](http://chimera.labs.oreilly.com/books/1230000000345/ch08.html):

	* D3's axes are actually functions whose parameters you define. Unlike scales, when an axis function is called, it doesn't return a value, but generate the visual elements of the axis, including lines, labels, and ticks.

	* Setting up an Axis:
		* _var xAxis = d3.svg.axis();_
		* At a minimum, each axis also needs to be told on what scale to operate on, so _xAxis.scale(xcale);_. We can also adjust the orientation of the labels (X axis: top, bottom, Y axis: left, right)

	* Once it is set up, we append it as an SVG group element "g":
		* _svg.append("g").call(xAxis);_. because an _axis_ function actually draws something to the screen (by appending SVG elements to the DOM), we need to specify where in the DOM it should place those new elements. This is in contrast to scale functions like xScale(), for example, which calculate a value and return those values, typically for use by yet another function, without impact the DOM at all.
		
		* a g element is a _group_ element. Group elements are invisible, unlike line, rect, and circle. and they have not visual presence. Yet they help us in two ways:
			* g elements can be used to contain other elements, which keeps our code nice and tidy.
			* we can apply _transformations_ to _g_ elements, which affects how visual elements within that group are rendered.
			* To learn more about _transformations_, check out [SVG transforms](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform). In this particular cases, we try to translate the axis from top to bottom by translating its axis anchor point.

		* the function _call()_ takes the incoming _selection_, as received from the prior link in the chain, and hands that selection off to any function as an argument. 

	* Cleaning up: we can even create a class for this "g" element and make configuration in CSS to style it. He also mentioned some conflicts between SVG / CSS naming, I am slightly confused.

	* We can specify _ticks(5)_ so that the axis only has 5 ticks. In fact, it will take tick as a suggestion, and find the optimal number of ticks, that might be slightly more or less than what you specified. This is very handy, as the data set change, d3 will make smart decision for you!

* [Interactive Data Visualization with D3.js: Chapter 9](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html):

	* This is perhaps the longest chapter in this e-book, and they cover the most important, and probably the strongest aspect of the d3.js library.
		
		* Until this point, we have used only static datasets. But real world data almost always _changes_ over time.
		* In D3 terms, those changes are handled by _updates_
		* The visual adjustments are made pretty with _transitions_, which can employ _motion_ for perceptual benefits.

	* I've already covered the section [_modernizing the bar chart_](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_modernizing_the_bar_chart). The basic idea here is again to leverage _scale_ and _axis_ to make the chart flexible enough to accomandate dataset of different size, domain, and range.

	* [**Updating Data**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_updating_data): I've also covered the concept of _event listener_, and how anonymous function can be used in response to an triggered event (e.g. click on a paragraph). In this chapter, the event listener has the following code pattern:
		
		* In response to the event, we:
			* Update the dataset
			* Update the DOM if necessary
			* Update the attributes of the DOM

	* [**Transition**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_transitions):
		
		* To add transition to the DOM elements:
			* Add _.transition()_ in the chain when your selection is made, and _above_ when any attribute changes are applied.
		
		* To prolong the animation time:
			* _duration()_ must be specified _after_ the _transition()_, and durations are always specified in milliseconds, so _duration(1000)_ is a one-second duration.
		
		* To change how transition is done:
			* _ease()_ must be specified after _transition()_, but before the _attr()_ statements to which the transition applies. They inlcude: _circle, elastic, bounce, ...etc_.
		
		* To delay the transition:
			* Simply use _delay(1000)_. As with _duration()_ and _ease()_, the order here is somewhat flexible, but it's good convention to include _delay()_ before _duration()_. Because delay happens first, followed by the transition duration itself.
			* _.delay(function(d,i){...})_ is also very common if you want the delay to vary depending on the datum (position) to make it smooth transition (wave of transitions).
			* Another point here is that _duration()_ sets the duration for each individual transition, not for all transitions in aggregate. So, for example, if 20 elements have 500-ms transitions applied with no delay, then it will all be over in 500 ms. But if a 100-ms delay is applied to each subsequent element (i * 100), then the total running time of all transition will be 2,400 ms.
			* This brings up the good point that often in _delay()_, we would do something like _.delay(function(d,i) { return i / dataset.length * 1000;})_ instead of letting the delay to grow arbitrarily big. 

		* [**Updating Scales**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_updating_scales)
			* We simply need to update the _d3.scale_ statement in the updating codes (anonymous function in the event listener)

		* [**Updating Axes**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_updating_axes)
			* Same trick, but since Axes are visual elements (remember the g object), we will need to select x.axis and y.axis objects and apply transition and duration on them.

		* each() transition starts and ends
			* There will be times when you want to make something happen at the start or end of a transition. In those times, _each()_ is handy to execute arbitrary code for each element in the selection. 
			* _each()_ expects two argument, either "start" or "end", and an anonymous function, to be executed either at the start of a transition, or as soon as it has ended.
			* Remember using another transition inside of _each()_ would break things. The reason is we always want the newest transition to override the old. In end, however, each("end", ...) does support transitions.
			* An equivalent way of doing transition + ease("end", transition) is to simply chain the transition without using ease.
			* A transtionless each() is also possible: this is useufl when you need to execute arbitrary code for each element in a selection.

	* [**Other Kinds of Data Updates**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_other_kinds_of_data_updates)
		
		* [**Adding Values**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_adding_values_and_elements). This section is worth reading again in person:
			* The insight here is that when we add a new value, we need to add a new DOM element, bind the data, and "enter" the new elments into the canvas.
				
				* **Select**: 
					* As usual. The twist here is that when we write _var bars = svg.selectAll("rect").data(dataset);_, the data() link actually returns references to all **elements** to which data was just bound, which we call the _update selection_.
				
				* **Enter**:  
					* The genius of the update selection is that it contains within it references to enter and exit subselections. In other words, it automatically tracks those additional elements AND those that needs to go away.
					* _**Whenever there are more data values than corresponding DOM elements, the enter selectio n contains references to those elements that do not yet exist**_. 

				* **Append**:
					* Since we have a direct reference to the new DOM elment that's yet to be added. All we need to do is the follow the _selectAll()->data()->enter()->append()_ pattern for the new element to be bind with the new data, and show up on the HTML.

				* Once the HTML work has been done (new DOM has been bound and added), we just use _transition()_ to transition all the attributes of these DOM elements to the right places, and we have successfully added a new value, to the dataset, and to the visualization, with nice animation and transition.

		* [**Removing Elements**](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_removing_values_and_elements)
			* Whenever there are more DOM elements than data values, the _exit_ selection contains references to those elements without data.

			* **Remove()**:
				* _bars.exit().transition().duration(500).attr("x", w).remove()_. Since bar.exit() points to the element that needs to be exit, we simply make a 500ms transition to move the element from where it is to x location the edge of the canvas at w.
				* Finally, _remove()_ is a special transition mehtod that waits until the transition is complete, and then deletes the element from the DOM forever.
			
			* Making the transition-out more smoothly (exit from the left for the first element in the array):
				* use the trick _.attr("x", -xScale.rangeBand())_
				* Not sure how _data joins with keys_ is related to all this. Whenever we call _data()_, a data join occurs that binds data with DOM elements. A data join with 'key' function gives us more control on the order.

		* Finally ,we can always [combine enter and exit](http://chimera.labs.oreilly.com/books/1230000000345/ch09.html#_add_and_remove_combo_platter).

	* **Recap**:
		* _data()_ binds data to elements, but also returns the **update selection**.
		* The update selection can contain _enter_ and _exit_ selections, which can be accessed via _enter()_ and _exit()_.
		* When there are _more values than elements_, an enter selection will reference the placeholder, not-yet-existing elements.
		* When there are _more elements than values_, an exit selection will reference the elements without data.
		* Data joins determine how values are matched with elements.
		* By default, data joins are performed by index, meaning in order of appearance.
		* For more control over data joins, you can specify a key function.
		* The sequence _enter, update, exit_ is not set in stone. Depending on your design goals, you might want to update first, then eneter new elements, and finally exit old ones. It all depends on what makes the most logical and aesthetic sense.

* [Interactive Data Visualization with D3.js: Chapter 10](http://chimera.labs.oreilly.com/books/1230000000345/ch10.html): This chapter is about "interactivity", i.e. making your graphs interactive using the construct of 'event listener' (which we briefly learned this in chapter 9). In this chapter, we discuss interactive examples such as how to highlight a particular 'rect' on a bar chart on 'mouseover' or 'mouseout'; how to re-sort the data and re-arrange them on 'mouseclick'; and how to provide different tooltip to surface 'details on demand'.

* **Event Listener**:
	* Just like we can bind data to DOM elements in d3, we can also **bind event listener to a single or multiple DOM elements**. 
	* The event listner construct is based on the 'event model' in Javascript, so D3 recognize all standard Javascript events, suc has 'mouseover', 'click' ... etc.
	* Remember, events don't happen in vacuum. They are always called on a specific element!
	* Event listener always take two part:
		* Defining particular event we care about
		* Defining the behavior to happen after the event occur
	* You can bind these event listeners right after when the element is created.

* **Example 1: highlighting**
	* One poor man's approach is to achieve this interactivity using CSS rules alone, no Javascript required. Check out the selector _:hover_.
	* Using the new CSS3 transitions, we can also apply some slow transition to the change.
	* Alternatively, we can do it with D3 and javascript by creating a event listener on 'mouseover' event. Inside the event listener, we define an anonymous function that changes the attribute of 'fill'.
		* In particular, the "this" construct is being used again. Just remember this: Within anonymous functions, D3 automatically sets the context of 'this' so it references “the current element upon which we are acting.”
		* We can also make sure the interactivity restore to the original color on 'mouseout'.
		* Feel free to add transition() and duration() to make the interactivity smoother.

* **Side note: Pointer events on overlapping elements**:
	* Mouse events are triggered only on elements with pixels that can be “touched” by the mouse. If two elements overlap, and the mouse moves over the element that is “on top” -- the mouseover event will be triggered on the frontmost element, and not on the element behind it.
	* Remember that in SVG, elements placed later in the DOM are rendered visually “in front” of earlier elements. This can make visual interaction counter-intuitive (see _06_smoother.html_). 
	* The solution is '_pointer-events: none' syntax in CSS rule. This says that this element shouldn't trigger any pointer events (such as click, mouseover, mouseout), so just behave as if the element is not there.
	* Alternatively, you can specify the style in d3 in element creation: _svg.append("text").style("pointer-events", "none");_.

* **Grouping SVG elements**:
	* Note that g group elements do not, by themselves, trigger any mouse events. The reason for this is that g elements have no pixels! Only their enclosed elements—like rects, circles, and text elements—have pixels.
	* However, this construct is handy. To avoid the inconsistency of overlapping elements, just put everything under 1 group, then we will not have that problem anymore!

* **Example 2: Click to Sort**:
	* This section demonstrate how we can wrap another custom sort function insdie the anonymous function in the event listener.
	* It also demonstrate the sort method upon a selection of DOM elements: _d3.selectAll("rect").sort(comparator function)_.
		* The important thing here is the comparator function, we need to let the sort function know how to sort. Luckily we have helper fucntions like d3.ascending or d3.descending. (Look how nested we hare (event_listener(anonymous function(custom sort(sort(comparator))))))! yay!).
	* One cool trick for this kind of re-ordering of data is to animate per-element delay use _delay(function(d, i) return i * 50;)_ (remember from Chapter 9?). This makes the whole re-ordering continuous and smooth. Very cool!
	* Also mentioned that sometimes if you have several interactivity on several events, the most recent event would take over. So often in design, we have to make choices so that they don't interfere. The solution in this example was to make highlight into CSS, and the rest as d3 transitions.
	* We can also sort in descending or ascending order by adding a little bit more codes.

* **Example 3: Tooltips**:
	* In interactive visualizations, tooltips are small overlays that present data values. In many cases, it’s not necessary to label every individual data value in the default view, but that level of detail should still be accessible to users. That’s where tooltips come in.
	* Default Browser Tooltip:
		* To make these tooltips, simply inject a title element into whatever element should have the tooltip applied
	* SVG Element Tooltip:
		* Many ways to do it, here the author demonstrate on each mouseover, a new value label is created, and on mouseout it's destroyed.
		* It's worth looking at how to destroy it on mouseout: _d3.select("#tooltip").remove();_
	* HTML div Tooltip:
		* use HTML tooltip when:
			* You want to achieve a visual effect that isn’t possible or well-supported with SVG (such as CSS drop shadows)
			* You need the tooltips to extend beyond the frame of the SVG image
		* Design pattern: 
			* Create a div, assigned it with #tooptip and #value ids.
            * style the div
            * Reference the #tooltip and #value id on mouseover event.
            * Use the 'hidden' class to show or hide the HTML tooltip.

* [Interactive Data Visualization with D3.js: Chapter 11](http://chimera.labs.oreilly.com/books/1230000000345/ch11.html): Today's chapter is about **layout**. Contrary to what the name implies, D3 layouts do not, in fact, lay anything out for you on the screen. The layout methods have no direct visual output. Rather, D3 layouts take data you provided and remap or otherwise transform it, thereby generating _new_ data that is more convenient for a specific visual task. It's still up to you to tak that new data and generate visuals from it.

	* [**Many examples on the D3 website**](https://github.com/mbostock/d3/wiki/Gallery)
	
	* [**The official API documentation**](https://github.com/mbostock/d3/wiki/Layouts)

	* In this chapter, we introduce 3 layouts:
		* Pie layout
		* Stack Chart layout
		* Force firected graph layout

	Chances are I am not going to remember the details, and will have to refer back to the example code again. I think the important thing here to try to load the examples, see how dataset was transformed after applying layouts on them.

* [Interactive Data Visualization with D3.js: Chapter 12](http://chimera.labs.oreilly.com/books/1230000000345/ch12.html): This chapter is about geomapping, codes are [here](https://github.com/alignedleft/d3-book/tree/master/chapter_12). Specifically, we learned:

	* **GeoJSON, a specific case of JSON files**:
		
		* GeoJSON is the JSON-based standard for encoding geodata for web applications.
		* In a typical GeoJSON style, we have an object type "FeatureCollection" as the key, followed by a value that is an array of "features" containing individual "feature objects". Each feature object contains type and geometry, under geometry we have specific coordinates of the path. See the structure from the textbook.
		* The convention is that longitude first, latitude second.
		* In case your cartographic skill are a bit rusty, here is how we remember which is which:
			* Latitude is fatitude, so they wrap around the earth's waist, so it's horizontal.
			* Longtitude is long, so they are vertical.

	* **Paths**: 
		
		* Using _d3.geo.path()_ to construct SVG _path generator_. It does all the dirty work of translating that mess of GeoJSON coordinates into even messier messes of SVG path codes.
		* _svg.selectAll("path").data(json.features).enter().append("path").attr("d", path)_ where _d_ is the path data attribute, and it refers to our path generator.

	* **Projection**:

		* Real world is 3d, projection help us to project 3d coordinates into a nice 2d space.
		* D3 has several built-in projection methods, 
		* Once you define the projection, make sure to reference it in d3.geo.path as _var path = d3.geo.path().projection(projection);_.
		* We can also shrink or expand projection using _.scale(1000)_. Default is 1000 px.

	* **Choropleth**:
		
		* Def: Choropleth are geomap with areas filled in with different values (light or dark) or colors to reflect associated data values. A classic example of election map "red state, blue state".
		* They are super-useful, bu have some inherent perceptual limitations. Because it uses _area_ to encode values, large areas with low density (e.g. Nevada) might be overrepresented visually, vice versa -- A standard choropleth does not represent per-capita values fairly.


		* d3.scale.quantize: act like a linear scale, but it outputs values from within a discrete range. These output values are often numbers or colors. This is useful for sorting values into "buckets". This is a common scale to use for choropleth.


		* The conventional way of reading GeoJSON for plotting is using _d3.json("filename", callback_function())_. If you don't remember this convention, read ["Handling Data Loading Errors"](http://chimera.labs.oreilly.com/books/1230000000345/ch05.html#_data). Remember this call is _asynchronous_, meaning it won't prevent the rest of your code from running while the browser waits for that external file to load. So be aware of calling this external data somewhere else (it might not have been loaded).
			* In fact, d3.csv and d3.json can be use together in nested fashion. In this particular example, we use this nested construct to **join** datasets together:
			* Recall how we delay calling domain on the d3.scale.quantize until we have the data loaded in the callback function! This reinforces the notion that callbacks are _asynchronous_.
			* With this joined data, we can map data to visual elements as usual. (color-code state by agriculture productivity) 
		

		* The "adding points" section follows the same code pattern:
			* We first load in the data using d3.json or d3.csv
			* Once the data is loaded in the callback, we map data to visual elements (map population size with the radius of the circles).
		
	* **Acquring and Parsing Geodata**: I didn't really follow every single step in this section since it requires installing some command line tools (I'm lazy). The basic steps involve:
		* Finding shapefiles
		* Choose a resolution that you think it's appropriate for your data viz
		* Sometimes we want to simplify the shapes by choosing a worse resolution. Remember, we don't want to load data that are too large into the browser because the rendering time might be delayed.
		* Convert it into GeoJSON
		* With the GeoJSON file at hand, you can do all the things we learn in earlier section to visualize!

* [Interactive Data Visualization with D3.js: Chapter 13](http://chimera.labs.oreilly.com/books/1230000000345/ch13.html): There is really not much going on here.

* [Interactive Data Visualization with D3.js: Appendix, Further Study](http://chimera.labs.oreilly.com/books/1230000000345/apa.html)
	* Book: Getting Started with D3 by Mike Dewar. I took a quick look of Amazon's review and the book's outline, it's not nearly as good as this one. I might not pursue this.
	* Websites:
		* Anything related to Mike Bostock example seems great. I copied down some examples and confirmed that things rendered well on my own browser. So I can technically just go through the examples myself.
		* github.com/mbostock/d3/wiki/API-Reference has detailed documentation on all the functions that I need.
		* There is also the d3 google group if I want to be up-to-date about d3's current developement
		* blog.visual.ly/creating-animations-and-transitions-with-d3-js/ -- a great tutorial on animation and transitions in d3


I haven't really decided yet what's next for D3, there is nothing obvious just yet. Keep searching!

