// This file has been modified to remove dependency on the external backend API.
// The logging function is now a no-op.

async function log(id, name, type) {
  // No-op: logging is disabled in static mode.
  // You can re-enable this if you have your own backend.
  console.log(`[Static Mode] Action: ${type}, Character: ${name} (${id})`);
  return Promise.resolve();
}

export default log;
