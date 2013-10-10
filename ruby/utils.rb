require 'time'

def prepare_intervals(duration)
  now = Time.now().utc()
  ago = now - duration
  [ago.iso8601, now.iso8601]
end