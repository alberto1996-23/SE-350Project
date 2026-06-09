// These are just reusable display components.

// Use them in:

// menu loading
// order status loading
// backend failure messages
type LoadingMessageProps = {
  message: string
}

function LoadingMessage({ message }: LoadingMessageProps) {
  // I use this to show a reusable loading banner anywhere in the app.
  return <div className="message-box loading">{message}</div>
}

export default LoadingMessage