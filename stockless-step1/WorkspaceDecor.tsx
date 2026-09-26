/* Decorative background for the workspace shell.

   The artwork lives in the two gutters beside the 1180px content column and
   nowhere else, so no wave, leaf or dot ever passes under a heading, a card or
   a table. Below 1330px there is no gutter left to draw in, so it is dropped
   rather than allowed behind the text. Colours are sampled from the StockLess
   background mockup; the wash fades to the page colour, which matches the
   homepage. Decorative only — it never takes a pointer event. */

function Leaf({ x, y, s, rot, fill, op }: {
  x: number; y: number; s: number; rot: number; fill: string; op: number;
}) {
  return (
    <g transform={`translate(${x} ${y}) rotate(${rot}) scale(${s})`} opacity={op}>
      <path d="M36 2C16 16 4 34 4 52c0 17 14 30 32 30s32-13 32-30C68 34 56 16 36 2Z" fill={fill} />
      <path d="M36 78V12" stroke="#FFFFFF" strokeOpacity=".5" strokeWidth="2.5" strokeLinecap="round" />
      <path d="M36 34 18 46M36 34l18 12M36 54 20 66M36 54l16 12"
        stroke="#FFFFFF" strokeOpacity=".3" strokeWidth="2" strokeLinecap="round" />
    </g>
  );
}

function Dots({ x, y }: { x: number; y: number }) {
  const circles = [];
  for (let i = 0; i < 3; i++) for (let j = 0; j < 4; j++)
    circles.push(<circle key={`${i}-${j}`} cx={i * 15} cy={j * 15} r="2.3" />);
  return <g transform={`translate(${x} ${y})`} fill="#9CC9A0" opacity=".5">{circles}</g>;
}

/** One gutter strip. The right-hand copy is mirrored in CSS. */
function Gutter({ id }: { id: string }) {
  return (
    <svg viewBox="0 0 160 900" preserveAspectRatio="xMinYMid slice">
      <defs>
        <linearGradient id={id} x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stopColor="#DCEFD8" stopOpacity=".6" />
          <stop offset=".5" stopColor="#EDF7E9" stopOpacity=".4" />
          <stop offset="1" stopColor="#FFFFFF" stopOpacity="0" />
        </linearGradient>
      </defs>
      <rect width="160" height="900" fill={`url(#${id})`} />
      {/* waves settle at the foot of the strip */}
      <path d="M0 900V688c50-28 102 16 160-4v216Z" fill="#B8DFBE" opacity=".45" />
      <path d="M0 900V772c54-24 106 18 160 0v128Z" fill="#83B480" opacity=".26" />
      <Leaf x={14} y={128} s={0.52} rot={-16} fill="#8FBC8B" op={0.55} />
      <Leaf x={86} y={236} s={0.34} rot={31} fill="#A5CDA0" op={0.5} />
      <Leaf x={22} y={556} s={0.44} rot={12} fill="#A6CEA4" op={0.5} />
      <Dots x={96} y={404} />
      <Dots x={18} y={392} />
    </svg>
  );
}

export function WorkspaceDecor() {
  return (
    <div className="ws-decor" aria-hidden="true">
      <div className="ws-decor__side ws-decor__side--left"><Gutter id="wsGutterL" /></div>
      <div className="ws-decor__side ws-decor__side--right"><Gutter id="wsGutterR" /></div>
    </div>
  );
}
