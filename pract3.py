def bayes_theorem(prior_prob, likelihood, evidence):
    # Calculate the posterior probability using Bayes' theorem
    posterior_prob = (likelihood * prior_prob) / evidence
    return posterior_prob

if __name__ == "__main__":
    
    # Given values
    prior_prob = 0.01 # Prior probability of having cancer
    likelihood_cancer = 0.95 # Likelihood of getting a positive test result given cancer
    likelihood_no_cancer = 0.10 # Likelihood of getting a positive test result given no cancer

    # Calculate the evidence using the law of total probability
    evidence = (likelihood_cancer * prior_prob) + (likelihood_no_cancer * (1 - prior_prob))

    # Calculate the posterior probability

    posterior_prob = bayes_theorem(prior_prob, likelihood_cancer, evidence)

    print("Prior Probability of Cancer:", prior_prob)
    print("Likelihood of Positive Test Given Cancer:", likelihood_cancer)
    print("Likelihood of Positive Test Given No Cancer:", likelihood_no_cancer)
    print("Posterior Probability of Cancer Given Positive Test:", round(posterior_prob, 2))
