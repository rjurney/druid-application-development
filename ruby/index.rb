# myapp.rb
require 'sinatra'
require 'druid'
require 'json'
require './utils'

set :public_folder, File.dirname(__FILE__) + '/static'
set :views, 'templates'

client = Druid::Client.new('', {:static_setup => { 'realtime/webstream' => 'http://localhost:8083/druid/v2/' }})

get '/timeseries' do
  intervals = prepare_intervals(60)
  query = Druid::Query.new('realtime/webstream').double_sum(:rows).granularity(:second).interval(intervals)
  result = client.send(query)
  jsonable = result.map {|r| {'timestamp' => r.timestamp, 'result' => r.row}}
  @json = JSON.generate(jsonable)
  puts @json
  erb :index
end
