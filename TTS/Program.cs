using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.IO;
using System.Net;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            HttpService service = new HttpService();
            byte[] response = service.GetAsync("Brian", "Testing TTS").Result;
            File.WriteAllBytes("./Name.mp3", response);
            Console.WriteLine(response);
            Console.WriteLine("KEY");
            Console.ReadKey();
            // Go to http://aka.ms/dotnet-get-started-console to continue learning how to build a console app! 
        }
    }
    public class HttpService
    {
        private static HttpClient sharedClient = new HttpClient()
        {
            BaseAddress = new Uri("https://api.streamelements.com/kappa/v2/speech?"),
            Timeout = TimeSpan.FromMinutes(0.5)
        };
        private static HttpClientHandler handler = new HttpClientHandler()
        {
            AutomaticDecompression = DecompressionMethods.GZip
        };
        

        public  async Task<byte[]> GetAsync(string voice, string text)
        {
            string baseUri = sharedClient.BaseAddress.ToString();
            using (HttpResponseMessage response = await sharedClient.GetAsync(baseUri + "voice=" + voice + "&text=" + text))
            { return await response.Content.ReadAsByteArrayAsync(); }
        }
    }
}
