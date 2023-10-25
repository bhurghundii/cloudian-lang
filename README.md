# Cloudian 

A minimal DSL to generate AWS Diagrams. 

## Motivations 

As a software engineer who works on distributed systems, I have to use tools like Draw.IO to generate diagrams.
I find a lot of drawing tools are well suited for being interfaced with hardware such as a mouse.

As someone who has a shoulder injury, I find using a mouse hard and painful. 

I was not able to find a simple text-based solution so I rolled my own. 


## Syntax 

You can: 
1) Declare AWS resources 
2) Get them to either point to things, or contain things. 

### Declare AWS resources 

```
    x::Resource
```

This declares a resource for the diagram of a certain type of AWS resource. 

Example:

```
    dynamodb::dynamodb
```

### Get them to either point to things, or contain things. 

```
    x => [A]
```

This declares relationship (goes to) for the resource to another resource 
Resources which are marked as "groups" mean that everything inside that [A] will go inside that resource. This is 
essentially how you create groups and subgroups. You can use this to create things like subnets and VPCs.

Example:

```
    dynamodb => [cognito]
```

Note: you have to have a list there 

### Some sugar 🍭

```
    x::Resource => [A]
```

This is just shorthand for create a resource and getting it to point somewhere / create a group. 

```
    region1::subnet => [amplify, cognito, storage]
```

## Precedence 

Items at the top of the file have a higher precedence than below. 
So if you want to have subnets in a region, you got to have them like:

```
    region1::subnet => [subnet-a]
    subnet-a::subnet => [s3]
```

The highest precedence is global, which you can access by not putting a resource in any group

## AWS resources supported 

See the /assets folder to see which symbols we got 

## Future 

Expect a web app editor to play around with this.
More expressiveness would be nice