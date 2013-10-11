require 'time'

def prepare_intervals(duration)
  now = Time.now().utc()
  ago = now - duration
  [ago.iso8601, now.iso8601]
end

def prepend_anchor(counts, dt)
  # To give us an empty margin, we need a 0.0 stamped at the left-most time edge, 
  # and right at the start of our data
  anchor = [{"timestamp" => dt.sub("Z", ".000Z"), "result" => {"rows" => 0.0}}]
  left_most = [{"timestamp" => counts[0]['timestamp'], "result" => {"rows" => 0.0}}]
  return anchor + left_most + counts
end