# index.rb
require 'sinatra'
require 'druid'
require 'json'

set :public_folder, File.dirname(__FILE__) + '/static'
set :views, 'templates'

client = Druid::Client.new('', {:static_setup => { 'realtime/webstream' => 'http://localhost:8083/druid/v2/' }})

def fetch_data(client, start_iso_date, end_iso_date)
  query = Druid::Query.new('realtime/webstream').time_series().double_sum(:rows).granularity(:second).interval(start_iso_date, end_iso_date)
  result = client.send(query)
  counts = result.map {|r| {'timestamp' => r.timestamp, 'result' => r.row}}
  json = JSON.generate(counts)
end

get '/time_series' do
  erb :index
end

get '/time_series_data/:start_iso_date/:end_iso_date' do |start_iso_date, end_iso_date|
  fetch_data(client, start_iso_date, end_iso_date)
end
