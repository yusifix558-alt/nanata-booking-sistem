import Link from "next/link";
import { Instagram, MessageCircle } from "lucide-react";

export default function Footer() {
  return (
    <footer className="bg-paper text-dark pt-20 pb-10 px-6 border-t border-dark">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
        <div className="lg:col-span-2 space-y-6">
          <Link href="/" className="inline-block">
            <span className="font-editorial text-3xl font-bold tracking-wide italic text-dark leading-none mb-1">
              Namata Studio<span className="text-namata-pink">.</span>
            </span>
          </Link>
          <p className="text-dark/70 font-sans text-sm leading-relaxed max-w-sm">
            Cantik sampai ke ujung jari. Tingkatkan rasa percaya dirimu dengan sentuhan nail art premium dan treatment bulu mata dari ahlinya.
          </p>
        </div>

        <div className="space-y-6">
          <h3 className="font-semibold tracking-[0.2em] text-[10px] text-dark/50 uppercase">Explore</h3>
          <ul className="space-y-3 text-[11px] font-medium tracking-wide text-dark">
            <li><Link href="/#treatments" className="hover:text-namata-pink transition-colors">Treatments</Link></li>
            <li><Link href="/#artists" className="hover:text-namata-pink transition-colors">Artists</Link></li>
            <li><Link href="/booking" className="hover:text-namata-pink transition-colors">Booking</Link></li>
          </ul>
        </div>

        <div className="space-y-6">
          <h3 className="font-semibold tracking-[0.2em] text-[10px] text-dark/50 uppercase">Connect</h3>
          <ul className="space-y-3 text-[11px] font-medium tracking-wide text-dark">
            <li>
              <a href="#" target="_blank" rel="noreferrer" className="flex items-center gap-2 hover:text-namata-pink transition-colors">
                <Instagram size={14} /> Instagram
              </a>
            </li>
            <li>
              <a href="https://wa.me/62881036695165" target="_blank" rel="noreferrer" className="flex items-center gap-2 hover:text-namata-pink transition-colors">
                <MessageCircle size={14} /> WhatsApp
              </a>
            </li>
          </ul>
        </div>
      </div>

      <div className="max-w-7xl mx-auto mt-20 pt-8 border-t border-dark/10 flex flex-col sm:flex-row justify-between items-center text-[10px] text-dark/40 uppercase tracking-widest">
        <p>&copy; 2026 Namata Studio. All rights reserved.</p>
        <p className="mt-2 sm:mt-0">Est. 2024</p>
      </div>
    </footer>
  );
}
