Constructing inverse diagrams in homotopical type theory
========================================================

Inverse diagrams, i.e. functors indexed by inverse categories, feature prominently in both the metatheory and applications of homotopical type theory (which we take to include MLTT without UIP, alongside the various incarnations of homotopy type theory). Besides their well known appearances as building blocks for higher categories and presheaf models of HoTT, they also give new model constructions (Shulman 2013, Kapulkin and Lumsdaine 2020), (homotopy) canonicity and parametricity results (Shulman 2013), and presentations of higher categorical structures with strict composition (Kock 2005).

The majority of the above results are developed in a classical metatheory, assuming UIP. We move the fundamental constructions of inverse diagrams and matching objects of Reedy fibrations into a constructive setting without UIP, by describing a construction of inverse diagrams in wild categories with families in HoTT. We develop some theory of wild cwfs, which form a common generalization of set-based and infinity-cwfs and thus include as examples both the syntax and the "standard" universe model. We then construct the matching object as a wild functor from cosieves in sufficiently nice inverse categories to categories of contexts of wild cwfs. This sets the stage for further development of an internalized metatheory of HoTT as well as investigations into the existence of semisimplicial types in plain HoTT.

----------------------------------------------------------------

Old draft
---------

Inverse diagrams, i.e. presheaves on inverse categories, are intimately connected to both the metatheory and the applications of homotopical type theory.
(By "homotopical type theory" (HoTT) I mean the class of dependent type theories which may be given semantics with nontrivial homotopical content; this includes MLTT without UIP as well as book HoTT.)

...

The constructions of (Kapulkin and Lumsdaine) and (Shulman) are given in CwA's and type theoretic fibration categories respectively, familiar models of HoTT in the setting of a "classical", "set theoretic" metatheory, where equality carries no higher homotopical content.
That is, the semantics of homotopical type theory are presented in terms of strict, set-level structures.

As an early step towards the goal of developing metatheory of HoTT in HoTT itself, we give a construction of inverse diagrams in wild categories with families internal to HoTT.
so that the preposition of the title refers both to our metatheory as well as the object theory.
