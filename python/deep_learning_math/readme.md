The standard way to avoid overfitting is called **L2 regularization**. It consists of appropriately modifying your cost function, from:

**Cost = Cross rntropy loss + L2_regularization loss**

**Exercise**: Implement `compute_cost_with_regularization()` which computes the cost
**Exercise**: Implement `backward_propagation_with_regularization()` which computes gradients with regularization(2)
