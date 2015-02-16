### Statistics Done Wrong Notes

Great notes, helped me to clarify and articulate some of the pitfalls in experimentation. A [new book] will be available in March 2015 which expands on a lot of the interesting points he brought up. The Author [Alex Reinhart] is a Statistics Ph.D student in CMU.

#### P-value, statistical significance, and practical significance

Without much surprises, the author started by introducing the concept of _**hypothesis testing**_, in an informal language, using testing the effectiveness of an medication as an example. He drove the point that we always started off by making an assumption (of the NULL hypothesis), what is the typical distribution of the metric I am interested in measuring. 

We then use _p-value_ as a **deductive reasoning** vehicle to learn how unlike we are going to observe what we observe (and more extreme). That’s a tricky concept to wrap your head around. **A p-value is not a measure of how right you are**, or how significant the difference is; it’s a measure of how _surprised_ you should be if there is no actual difference between the groups, but you got data suggesting there is. A bigger difference, or one backed up by more data, suggests more surprise and a smaller p value.

* **Here comes the learning:**, it's not easy to translate p-value into an answer to the question "is there really a difference?"
	
	*  Most scientists use a simple rule of thumb: if p is less than 0.05, there’s only a 5% chance of obtaining this data unless the medication really works, so we will call the difference between medication and placebo “significant.” If p is larger, we’ll call the difference insignificant.

	* But there are limitations. _The p value is a measure of surprise, not a measure of the **size of the effect**_. 
		* I can get a tiny p value by either measuring a huge effect – “this medicine makes people live four times longer”
		* or by measuring a tiny effect with great certainty. 

	Statistical significance does not mean your result has any practical significance.

	* Similarly, statistical insignificance is hard to interpret.
		* I could have a perfectly good medicine, but if I test it on ten people, I’d be hard-pressed to tell the difference between a real improvement in the patients and plain good luck. (AKA low-powered test)
		* Alternately, I might test it on thousands of people, but the medication only shortens colds by three minutes, and so I’m simply incapable of detecting the difference. A statistically insignificant difference does not mean there is no difference at all.

There’s no mathematical tool to tell you if your hypothesis is true; you can only see whether it is consistent with the data, and if the data is sparse or unclear, your conclusions are uncertain.



#### Statistical Power 

We’ve seen that it’s possible to miss a real effect simply by not taking enough data. In most cases, this is a problem: we might miss a viable medicine or fail to notice an important side-effect. How do we know how much data to collect? Here comes the concept of Statistical Power -- _The power of a study is the likelihood that it will distinguish an effect of a certain size from pure luck._

He later used the coin flipping example & power curve to demonstrate his point:
	* If we have a coin that is completely unfair, the chance of us detecting the bias coin with just 10 flips is high
	* If we have a coin that is nearly fair, the chance of us detecting the small bias with just 10 flips is abysmally small

He later demonstrate how the power curve changes as a function of the number of flips, from 10, to 100, and then 1000. See [power curve]. I love this section, because I often think in this way as well.

Getting adequate sample size is important, and sometimes researcher try to replicate more data to increase the sample size. But then we are likely to run into the problem of **psuedo-replication** -- which happens when individual observations are heavily dependent on each other. Your measurement of a patient’s blood pressure will be highly related to his blood pressure yesterday, and your measurement of soil composition here will be highly correlated with your measurement five feet away. The Author also provided some [suggestions how to avoid psuedoreplication]

#### The p-value and the base fallacy

We've already seen that p values are hard to interpret. Getting a statistically insignificant result doesn’t mean there’s no difference (It might be that we have low power and/or the effect size is too small to be detected). What about getting a significant result?

The Author gave a very good visual representation about the problem, using a [10-10 grid] to demonstrate his point. And here is his point -- Given that we observed a statistically significant result, the chance of having a false positive is actually ~38% (8/(8+5)). 

Because the base rate of effective cancer drugs is so low – only 10% of our hundred trial drugs actually work – most of the tested drugs do not work, and we have many opportunities for false positives. Think about the extreme case, if I had the bad fortune of possessing a truckload of completely ineffective medicines, giving a base rate of 0%, there is a 0% chance that any statistically significant result is true -- type I error (false positives) is inherent in the testing framework, and they can be lurked together with true positives and it's hard to distinguish the two.

You often hear people quoting p values as a sign that error is unlikely. “There’s only a 1 in 10,000 chance this result arose as a statistical fluke,” they say, because they got p=0.0001. No! This ignores the base rate, and is called the **base rate fallacy**. 

IMO, I think the disconnect here is that people are confusing the question we are trying to answer and the definition of p-value:
	1. What they are asking: P(alternative is true | observed statistically significant result)
	2. What p value is: P(seeing something as extreme as what we observed), given that there is no difference

These two questions are completely different. And notice how we intuitively anser the first question:

```python
P(alternative is true | observed statistically significant result) = 

P(observed stat sig result | alternative is true) * P(alternative is true) / P(observed statistically significant result) = 
P(observed stat sig result | alternative is true) * P(alternative is true) / P(stat sig | null is true) * P(null is true) + P(stat sig | alternative is true) * P(alternative is true)
```
But even then I think this way of thinking is quite weird, the concept of P(alternative is true) or P(null is true) is just weird in a frequentist perspective. I think the Bayesian thinking is more natural here.


#### Multiple Testing

The green jellybeans example demonstrated the point, when you run a bunch of tests, the chance of having at least one false positive is going to be increasing like crazy. A popular approach is **Bonferroni Correction**, where we divide the significance level by the number of tests we run, but this often runs into the problem of having too conservative criteria (it greatly decrease the power).

In reality, scientists are more interested in the false discovery rate: what fraction of my statistically significant results are false positives? Is there a statistical test that will let me control this fraction? Here comes Benjamini and Hochberg:

* Perform your statistical tests and get the p value for each. Make a list and sort it in ascending order.
Choose a false-discovery rate and call it `q`. Call the number of statistical tests `m`.
* Find the largest p value such that `p ≤ iq/m`, where `i` is the p value’s place in the sorted list.
* Call that p value and all smaller than it statistically significant.

You’re done! The procedure guarantees that out of all statistically significant results, no more than `q` percent will be false positives.

#### When differences in significance aren’t significant differences

The setting is the following: When compare A to control, A shows statistically significant result. When B is compared to control, there is no statistically significant result, does it necessarily means A is better than B. The short answer is No, be careful comparing the significance of two results. If you want to compare two treatments or effects, compare them directly.

“We compared treatments A and B with a placebo. Treatment A showed a significant benefit over placebo, while treatment B had no statistically significant benefit. Therefore, treatment A is better than treatment B.” We hear this all the time. It’s an easy way of comparing medications, surgical interventions, therapies, and experimental results. It’s straightforward. It seems to make sense. However, a difference in significance does not always make a significant difference. This question is very similar from _START team PM for Raghav_.

#### When significant differences are missed

Another typical mistake is that people just compare if the confidence interval of two statistics across two buckets overlap with each other. If they do, then they claim that there is no difference between the two groups, otherwise there is.

This is also wrong. My intuitive explanation is that the length of the confidence interval is a function of sample size, the more sample size, the smaller the width. You can imagine a scenario where there is truly a difference between the two buckets, but because we didn't have enough sample size, their CI overlaps with each other. Had you have more sample size, the critera of whether CIs overlap with each other would give two completely different result, so this criteria cannot be right.

Unfortunately, many scientists skip hypothesis tests and simply glance at plots to see if confidence intervals overlap. This is actually a much more conservative test – requiring confidence intervals to not overlap is akin to requiring p < 0.01 in some cases(?). It is easy to claim two measurements are not significantly different even when they are.

#### Early Stopping Rules leads to unneccesary optimism (Truth Inflation)

Like the section title suggested, early stopping rule might lead to more false positive. See the [timeseries] of the p-value as a function of the number of samples as an example.

This plot shows the p value of the difference between groups as we collect more data, with the horizontal line indicating the p=0.05 level of significance. At first, there appears to be no significant difference. Then we collect more data and conclude there is. If we were to stop, we’d be misled: we’d believe there is a significant difference between groups when there is none. As we collect yet more data, we realize we were mistaken – but then a bit of luck leads us back to a false positive.

ANother problem with this practice is Truth inflation. This happens when there is a effect, but because you had small sample size and you ended the experiment as soon as you get a significant result, the effect size you observed are likely to be inflated, even though you are making the correct conclusion.



[Alex Reinhart]: http://www.refsmmat.com/
[new book]: http://www.nostarch.com/statsdonewrong
[power curve]: http://www.statisticsdonewrong.com/power.html
[suggestions how to avoid psuedoreplication]: http://www.statisticsdonewrong.com/pseudoreplication.html
[10-10 grid]: http://www.statisticsdonewrong.com/p-value.html 
[timeseries]: http://www.statisticsdonewrong.com/regression.html