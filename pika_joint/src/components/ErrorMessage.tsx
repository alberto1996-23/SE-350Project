// These are just reusable display components.

// Use them in:

// menu loading
// order status loading
// backend failure messages
type ErrorMessageProps = {
  message: string
}

function ErrorMessage({ message }: ErrorMessageProps) {
  // I use this to show a reusable error banner anywhere in the app.
  return <div className="message-box error">{message}</div>
}

export default ErrorMessage