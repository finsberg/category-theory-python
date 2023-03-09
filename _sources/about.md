# Category theory
Category theory is probably the most abstract form of mathematics
there is. It is the theory that tries to unite all areas of mathematics.
It turns out that many concepts that arises in different areas of mathematics
share some common properties. That is, if your know about a relation in
set theory, then there is a similar relation in logic, or algebra.

From a programmers perspective, category theory is interesting because
we can use it to study type theory.

## Category

A category is a collection of objects that are linked by arrows.
We typically refer the the arrows as morphisms, and if you have knowledge
of higher mathematics, you know that there exists different types of morphisms,
such as isomorphisms, homomorphisms, homeomorphism, etc.

In the category of sets the objects would typically be sets, and the arrows
could be regular functions, i.e mappings from one set into another.


There are two axioms for a category

1. If there exist $f : a \mapsto b$ and $g : b \mapsto c$ then there exist
$h : a \mapsto c$, such that $h = g \circ f$ (the composition).
2. For each object $x$ in the category there exist an arrow, called the
identity arrow $1_x: x \mapsto x$, such that for every morphism
$f : a \mapsto b$ we have $1_x \circ f = f$ and for every morphism
$g : b \mapsto x$ we have $g \circ 1_x = g$.
