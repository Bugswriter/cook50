#!/bin/sh

curl -d "n=Hot Dog&r=2&d=Easy&rt=Dinner&pt=20&mi=Dog, Hot&rl=www.foody.com/hot-dog" \
     http://127.0.0.1:5000/add_recipe
