# Hash Backend Challenge

Hello and thanks for taking time to try this out.

The goal of this test is to assert (to some degree) your coding and architectural skills. You're given a simple problem so you can focus on showcasing development techniques and distributed systems knowledge.


You are **allowed** to use any sort of framework or library, but be prepared to answer some questions about those libraries, like why you chose them and what other alternatives you're familiar with. At Hash knowing how his/her work tools work is really important! 


Send the result of your challenge to dev@hash.com.br (the repo can be open source). Before a week we'll contact you to schedule an interview!


## Task

Write two microservices that together powers an web page that displays a product list with custom discounts per user.

__Restrictions__

1. The services **must** be written in distinct programming languages.
2. The services **must** communicate via [gRPC](https://grpc.io/)

### Service 1: Discount calculator

This service **must** receive two RPC arguments:
  - product_id: The ID of a Product
  - user_id: The ID of an User

Sample product schema:

```
{
    id: string
    price_in_cents: int
    title: string
    description: string
    discount: {
        pct: float
        value_in_cents: int
    }
}
```

Sample user schema:

```
{
    id: string
    first_name: string
    last_name: string
    date_of_birth: Date
}
```

The returned discount **must** obey the following rules:
  * If it's the user’s birthday, the product has 5% discount.
  * If it is black friday (for this test you can assume BlackFriday is November 25th), the product has 10% discount
  * No product discount can be bigger than 10%

  
  ### Service 2: Products list

This service exposes a HTTP endpoint `GET /product` that returns a list of products.

1. The endpoint response **must** be `JSON` encoded.
2. To calculate each product discount the service **must** consume service 1 via gRPC.
3. If service 1 errors while calculating a discount, the service **must** returns the product list but with zero discounts for the affected products.

## Evaluation Criteria
1. The problems are solved efficiently and effectively, the application works as expected.
2. The application is supplied with the setup scripts. Consider using docker and a one-liner setup.
3. You demonstrate the knowledge on how to test the critical parts of the application. We **do not require** 100% coverage.
4. The application is well and logically organised.
5. The submission is accompanied by documentation with the reasoning on the decisions taken.
6. The code is documented and is easy to follow.
7. Following the industry standard style guide.
8. A git history (even if brief) with clear, concise commit messages.

Also if you'd like to know more about our developer culture, how we think and work in terms of development, check out our  [key values](https://www.keyvalues.com/hash).
