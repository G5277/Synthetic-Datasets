import pandas as pd
import random
import itertools

phishing_subjects = [
    "Urgent! Verify your account now", "Your password will expire soon!", "Suspicious login detected on your account",
    "Claim your free gift card today!", "Your PayPal account has been suspended", "New security alert: Immediate action required",
    "Payment failed: Update your billing details", "Congratulations! You have won a prize!", "Your order has been canceled",
    "Limited-time offer! Claim your bonus now", "Account security breach detected", "Unauthorized access attempt detected",
    "Confirm your identity to prevent deactivation", "Important notice: Update your credentials", "Unusual activity detected on your account"
]
legitimate_subjects = [
    "Your monthly bank statement is ready", "Meeting rescheduled to next week", "Welcome to our service!",
    "Invoice for your recent purchase", "Security update: New features available", "Friendly reminder: Upcoming event",
    "Team meeting scheduled for tomorrow", "Subscription renewal confirmation", "Thank you for your recent purchase",
    "Account activity summary available", "Upcoming maintenance alert", "Important security notice for your account",
    "Your delivery is scheduled", "Billing confirmation for your service", "We appreciate your feedback!"
]

phishing_senders = [
    "support@secure-b4nk.com", "admin@paypal-security.com", "account@amazon-verification.com",
    "lottery@big-win.com", "security@facebook-help.com", "service@banking-alert.com",
    "info@claim-reward.com", "verification@secure-portal.com", "no-reply@payment-failure.com",
    "alerts@fraud-detection.com", "urgent@finance-support.com", "help@banking-security.com",
    "accounts@secure-login.com", "support@funds-transfer.com", "service@order-cancellation.com"
]
legitimate_senders = [
    "support@bank.com", "admin@paypal.com", "contact@amazon.com", "newsletter@company.com",
    "security@facebook.com", "info@officialnews.com", "team@corporate-mail.com",
    "no-reply@billing.com", "support@subscription.com", "service@trusted-payment.com",
    "alerts@finance-notice.com", "notification@banking-updates.com", "contact@customer-support.com",
    "care@verified-service.com", "updates@official-source.com"
]

phishing_bodies = [
    "Click the link below to verify your account immediately!", "We've detected unauthorized access. Reset your password now!",
    "You have won a lucky draw! Claim your prize here.", "Update your billing information to avoid service interruption.",
    "Your account has been locked. Click below to restore access.", "Your payment has been declined. Confirm your details.",
    "Your account will be suspended if no action is taken within 24 hours.", "Your package delivery failed. Confirm your address.",
    "Exclusive offer: Redeem your coupon before it expires!", "Suspicious login detected: Secure your account now!",
    "Confirm your email for a security upgrade", "Get exclusive VIP benefits now!", "Your loan application has been pre-approved!",
    "Congratulations! You're eligible for a special discount", "Security alert: Your password has been compromised"
]
legitimate_bodies = [
    "Your monthly statement is attached. Let us know if you have questions.", "Meeting is rescheduled to next Tuesday. Please confirm your availability.",
    "Thanks for signing up! Here are some useful resources to get started.", "Your invoice for this month's subscription is available in your dashboard.",
    "We've updated our security features. No action is required on your part.", "Reminder: Your service plan has been renewed successfully.",
    "Your order has been shipped. Track your package here.", "Join us for our upcoming webinar. Click here to register.",
    "Important: Policy changes you should be aware of.", "Your feedback is important to us. Participate in our survey!",
    "Automatic bill payment confirmation", "Your subscription has been successfully renewed", "We have received your support request",
    "Friendly reminder: Your account is in good standing", "Enjoy new features in your latest app update"
]

def generate_synthetic_email_data(num_samples=8000):
    unique_combinations = list(itertools.product(phishing_subjects, phishing_senders, phishing_bodies)) + \
                         list(itertools.product(legitimate_subjects, legitimate_senders, legitimate_bodies))
    random.shuffle(unique_combinations)
    
    if len(unique_combinations) > num_samples:
        unique_combinations = unique_combinations[:num_samples]
    
    data = [[subject, sender, body, 1 if (subject in phishing_subjects) else 0] for subject, sender, body in unique_combinations]
    
    return pd.DataFrame(data, columns=["Subject", "Sender", "Body", "Label"])

# Generate dataset and save it to CSV
df = generate_synthetic_email_data(8000)
df.to_csv("./Data/synthetic_phishing_dataset.csv", index=False)

print("Synthetic phishing dataset created with unique entries: synthetic_phishing_dataset.csv")
