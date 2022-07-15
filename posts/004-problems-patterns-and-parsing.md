# Problems, patterns and parsing

Most problems have a structure, but often this structure is not obvious. So we look for patterns to determine the structure of the problem.

The simplest way I'm going to explain a pattern is by this: (0909090909). This may look like a random string of 0's and 9's but look! everytime there's a 0, there's a 9, that's a pattern.

Language also has structure, but what makes up this structure? **Grammer** and **punctuation**. Every language has like domain, but what is a domain? Let's say you are pasta legend, if someone asked you something about pasta you would probably know, because it's in your **domain**, so you would say: yeah I know what your talking about and give an answer, also known as the **range**. Now let's say they asked you about steak, you probably wouldn't know the answer to their question, because what they are asking is not in your domain!

Take for example the problem of answering a question that asks us to convert from centimeters to inches. The question can be asked in so many different ways, as can be seen below:

```
1. 1cm to in
2. cm to inches
3. centimeters to inches
4. 1cm   in
5. cm   in
6. 2 cm  in
7. 1 cm  in
```

How do we find what's common in the above list?

This is where parsing comes in handy. parsing is the analyzation of a string of characters. The act of parsing results in tokens of interest. I can explain tokens is like this: So when you go to some place like Chucky Cheese you exchange money for tokens, so you are taking one thing and turning it into something else!

So now lets parse! But first, let's list the tokens of interest to us.

1. let one or more digits `[0...9]+` be `N`
2. let `cm` be `A`
3. let `to` be `B`
4. let `in` be `C`
5. let `inches` be `D`
6. let `centimeters` be `E`
7. And finally `␢` represent the blank space

Now the search: "1cm to in" can be represented using our tokens and it looks like this:

1. `NA␢B␢C`

And likewise the rest of our list can `tokenized` as below:

2. `A␢B␢D`
3. `E␢B␢D`
4. `A␢␢␢C`
5. `A␢␢␢C`
6. `N␢A␢␢C`
7. `N␢A␢␢C`

Even with this I don't think I can see a pattern, so let's shorten it up. Let's create some higher order tokens:

> What the heck is a higher order token?
>
> Let's say you had 25 pennies. You exchange them for a nickel and 2 dimes or a quarter. In this example, the nickel, the dime, and the quarter would be the equivalent to a higher order token!

```
(A,E) => X
(C,D) => Y
(B)   => ␢ ; because this provides no significant information
[␢]+  => ␢ ; the blanks are worthless and can be deflated down to 1 ;-)
```

Now with these new higher order tokens, it looks like this:

1. `NX␢Y`
2. `X␢Y`
3. `X␢Y`
4. `NX␢Y`
5. `X␢Y`
6. `N␢X␢Y`
7. `N␢X␢Y`

Now a few patterns emerge, so in the end we reduce our original list down to:

1. `NX␢Y`  (3 tokens)
2. `X␢Y`   (2 tokens)
3. `NX␢Y`  (3 tokens)
4. `N␢X␢Y` (3 tokens)

That seems to be a lot of work to reduce a list 7 variations down to 4. But once we know how to
parse out `X` and `Y`, we can parse anything; for example `kilo` instead of `cm` and `pounds` instead of `inches`.

Finally we are ready to program with all the insights we gained from examining the structure of the problem.