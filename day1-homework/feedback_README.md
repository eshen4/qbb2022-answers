Question 3: So the awk command isn't quite printing col1, col2, and the difference between them. Let's look at what it's printing: `{print $1,$2-1, $2}`. So it's printing col1, then it's printing col2 - 1 (rather than col1), then it's printing col2. Thinking about the data that's stored in the vcf file, does it make sense to print col2 minus col1? Otherwise, really great work!

Nice job!
