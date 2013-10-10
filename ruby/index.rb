# myapp.rb
require 'sinatra'
require 'druid'
require 'json'
require './utils'

set :public_folder, File.dirname(__FILE__) + '/static'
set :views, 'templates'

client = Druid::Client.new('', {:static_setup => { 'realtime/webstream' => 'http://localhost:8083/druid/v2/' }})

def fetch_data(client)
  intervals = prepare_intervals(600)
  puts intervals
  query = Druid::Query.new('realtime/webstream').time_series().double_sum(:rows).granularity(:second).interval(intervals)
  result = client.send(query)
  puts result
  jsonable = result.map {|r| {'timestamp' => r.timestamp, 'result' => r.row}}
  json = JSON.generate(jsonable)
end

get '/time_series' do
  @json = fetch_data(client)
  #puts @json
  erb :index
end

get '/time_series_data' do
  fetch_data(client)
end
